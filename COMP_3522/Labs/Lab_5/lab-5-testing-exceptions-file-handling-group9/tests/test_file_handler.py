import os
import pathlib
from unittest import TestCase
from unittest.mock import patch, mock_open

from driver import Dictionary
from file_handler import FileHandler, FileExtensions, FileEnumMismatchError, InvalidFileTypeError


class TestFileHandler(TestCase):

    @patch('pathlib.Path.exists', return_value=True)
    def test_load_data_successfully_load_json(self, _):
        test_json = ('{"word1": ["definition1_1", "definition1_2"], '
                     '"word2": ["definition2_1", "definition2_2"]}')
        expected_data = {
            "word1": ["definition1_1", "definition1_2"],
            "word2": ["definition2_1", "definition2_2"]
        }

        with patch('builtins.open', mock_open(read_data=test_json)) as mocked_open:
            actual_data = FileHandler.load_data("file.json", FileExtensions.JSON)

        mocked_open.assert_called_once_with(pathlib.Path("file.json"), mode="r", encoding="utf-8")
        self.assertDictEqual(expected_data, actual_data)

    @patch('pathlib.Path.exists', return_value=True)
    def test_load_data_successfully_load_text(self, _):
        test_text = ("WORD1\n======\n1. definition1_1\n2. definition1_2\n"
                     "WORD2\n======\n1. definition2_1\n2. definition2_2\n")
        expected_data = {
            "word1": ["definition1_1", "definition1_2"],
            "word2": ["definition2_1", "definition2_2"]
        }

        with patch('builtins.open', mock_open(read_data=test_text)) as mocked_open:
            actual_data = FileHandler.load_data("file.txt", FileExtensions.TXT)

        mocked_open.assert_called_once_with(pathlib.Path("file.txt"), mode="r", encoding="utf-8")
        self.assertDictEqual(expected_data, actual_data)

    @patch('pathlib.Path.exists', return_value=True)
    def test_load_data_text_file_with_json_enum(self, _):
        test_text = ("WORD1\n======\n1. definition1_1\n2. definition1_2\n"
                     "WORD2\n======\n1. definition2_1\n2. definition2_2\n")
        expected_error_message = ("Provided path (file.txt) does not match provided "
                                  "file_extension_enum json.")

        with patch('builtins.open', mock_open(read_data=test_text)) as mocked_open:
            with self.assertRaises(FileEnumMismatchError, msg=expected_error_message):
                FileHandler.load_data("file.txt", FileExtensions.JSON)

        mocked_open.assert_not_called()

    @patch('pathlib.Path.exists', return_value=True)
    def test_load_data_json_file_with_txt_enum(self, _):
        test_json = ('{"word1": ["definition1_1", "definition1_2"], '
                     '"word2": ["definition2_1", "definition2_2"]}')
        expected_error_message = ("Provided path (file.json) does not match provided "
                                  "file_extension_enum txt.")

        with patch('builtins.open', mock_open(read_data=test_json)) as mocked_open:
            with self.assertRaises(FileEnumMismatchError, msg=expected_error_message):
                FileHandler.load_data("file.json", FileExtensions.TXT)

        mocked_open.assert_not_called()

    @patch('pathlib.Path.exists', return_value=True)
    def test_load_data_invalid_file_extension(self, _):
        test_text = ("WORD1\n======\n1. definition1_1\n2. definition1_2\n"
                     "WORD2\n======\n1. definition2_1\n2. definition2_2\n")
        expected_error_message = ("jpg is not a valid file extension. "
                                  "Please provide a .txt or .json file.")

        with patch('builtins.open', mock_open(read_data=test_text)) as mocked_open:
            with self.assertRaises(InvalidFileTypeError, msg=expected_error_message):
                FileHandler.load_data("file.jpg", FileExtensions.TXT)

        mocked_open.assert_not_called()

    def test_load_data_nonexistent_file(self):
        test_json = ('{"word1": ["definition1_1", "definition1_2"], '
                     '"word2": ["definition2_1", "definition2_2"]}')
        expected_error_message = "File file.json does not exist."

        with patch('builtins.open', mock_open(read_data=test_json)) as mocked_open:
            with self.assertRaises(FileNotFoundError, msg=expected_error_message):
                FileHandler.load_data("file.json", FileExtensions.JSON)

        mocked_open.assert_not_called()

    def test_parse_dictionary_from_text_one_entry(self):
        test_file_lines = [
            "WORD1\n", "======\n", "1. definition1_1\n", "2. definition1_2\n",
        ]
        expected_dictionary = {
            "word1": ["definition1_1", "definition1_2"],
        }

        actual_dictionary = FileHandler._parse_dictionary_from_text(test_file_lines)

        self.assertDictEqual(expected_dictionary, actual_dictionary)

    def test_parse_dictionary_from_text_multiple_entries(self):
        test_file_lines = [
            "WORD1\n", "======\n", "1. This is definition1_1\n", "2. definition1_2\n",
            "WORD2\n", "======\n", "1. definition2_1\n",
            "WORD3\n", "======\n", "1. definition3_1\n", "20. definition3_2\n",
        ]
        expected_dictionary = {
            "word1": ["This is definition1_1", "definition1_2"],
            "word2": ["definition2_1"],
            "word3": ["definition3_1", "definition3_2"]
        }

        actual_dictionary = FileHandler._parse_dictionary_from_text(test_file_lines)

        self.assertDictEqual(expected_dictionary, actual_dictionary)

    def test_write_lines_file_name_fail(self):
        try:
            test = FileHandler.write_lines("fakepath.xlx", "Line 1")
            self.fail()
        except InvalidFileTypeError:
            self.assertTrue(True)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_lines_txt(self, file):
        lines = ["Line 1", "Line 2", "Line 3"]
        FileHandler.write_lines("path.txt", lines)
        results = file()
        calls = [call.args[0] for call in results.write.call_args_list]

        self.assertEqual(calls, ["Line 1\n", "Line 2\n", "Line 3\n"])

    @patch('builtins.open', new_callable=mock_open)
    def test_write_lines_preexisting_file(self, file):
        lines = ["Line 1", "Line 2", "Line 3"]
        lines_to_add = ["Line 4", "Line 5", "Line 6"]
        FileHandler.write_lines("path.txt", lines)
        FileHandler.write_lines("path.txt", lines_to_add)
        results = file()
        calls = [call.args[0] for call in results.write.call_args_list]
        self.assertEqual(calls, ['Line 1\n', 'Line 2\n', 'Line 3\n', 'Line 4\n', 'Line 5\n', 'Line 6\n'])

    def test_save_query_result_writes_lines(self):
        expected_result = {'additive': ['A substance mixed in small quantities with another product to '
              'modify its chemical or physical state, for example to make food '
              'look visually more attractive.',
              'Proper to be added.']}
        dic = Dictionary()
        dic.load_dictionary("../data.json")
        definitions = dic.query_definitions("additive")
        query_output = dic.display_definitions("additive", definitions)
        dic.save_query_result(query_output, "test_results.txt")
        result = FileHandler.load_data("test_results.txt", FileExtensions.TXT)
        os.remove("test_results.txt")
        self.assertEqual(result, expected_result)
