from unittest import TestCase
from unittest.mock import patch, mock_open
from driver import Dictionary
from file_handler import FileHandler, FileExtensions, InvalidFileTypeError


class TestDictionary(TestCase):

    def setUp(self):
        self.dictionary = Dictionary()

        self.test_data = {
            "python": ["A programming language."],
            "test": ["A procedure."],
            "hello": ["Used as a greeting."]
        }

    def test_init(self):
        self.assertDictEqual(self.dictionary.data, {})
        self.assertFalse(self.dictionary.is_loaded)
        self.assertEqual(self.dictionary.query_history, [])

    @patch('driver.FileHandler.load_data')
    def test_load_dictionary_successfully_load_json(self, mock_load_data):
        mock_load_data.return_value = self.test_data
        self.dictionary.load_dictionary("data.json")
        self.assertDictEqual(self.dictionary.data,  self.test_data)
        self.assertTrue(self.dictionary.is_loaded)

    @patch('driver.FileHandler.load_data')
    def test_load_dictionary_successfully_load_txt(self, mock_load_data):
        mock_load_data.return_value = self.test_data
        self.dictionary.load_dictionary("data.txt")
        self.assertDictEqual(self.dictionary.data, self.test_data)
        self.assertTrue(self.dictionary.is_loaded)


    def test_load_dictionary_invalid_file_extension(self):
       expected_error_message = ("pdf is not a valid file extension. "
                              "Please provide a .txt or .json file.")

       with self.assertRaises(InvalidFileTypeError, msg=expected_error_message):
        self.dictionary.load_dictionary("data.pdf")

       self.assertFalse(self.dictionary.is_loaded)



    def test_query_definitions_found(self):
      self.dictionary.data = self.test_data
      actual_definitions = self.dictionary.query_definitions("test")
      expected_definitions = ["A procedure."]
      self.assertEqual(actual_definitions, expected_definitions)


    def test_query_definitions_not_found(self):
     self.dictionary.data = self.test_data
     actual_definitions = self.dictionary.query_definitions("nonexistent")
     self.assertEqual(actual_definitions, [])

    def test_query_case_insensitive(self):
      self.dictionary.data = self.test_data

      result1 = self.dictionary.query_definitions("python")
      result2 = self.dictionary.query_definitions("PYTHON")
      result3 = self.dictionary.query_definitions("PyThOn")
      self.assertEqual(result1, result2)
      self.assertEqual(result1, result3)


    @patch('driver.FileHandler.write_lines')
    def test_save_query_result(self, mock_write_lines):
        result = "\nPYTHON\n======\n1. A programming language.\n"
        self.dictionary.save_query_result(result)
        mock_write_lines.assert_called_once()


    def test_query_definitions_word_found_multiple_definitions(self):
      test_data_multiple = {
        "python": ["A programming language.", "A large snake."]
          }
      self.dictionary.data = test_data_multiple
      actual_definitions = self.dictionary.query_definitions("python")
      self.assertEqual(len(actual_definitions), 2)
      self.assertIn("A programming language.", actual_definitions)
      self.assertIn("A large snake.", actual_definitions)


    def test_query_history_tracks_queries(self):
        self.dictionary.data = self.test_data
        self.dictionary.query_definitions("python")
        self.dictionary.query_definitions("test")
        self.assertEqual(len(self.dictionary.query_history), 2)
        self.assertEqual(self.dictionary.query_history[0][0], "python")
        self.assertEqual(self.dictionary.query_history[1][0], "test")

    def test_display_definitions_word_found(self):
        definitions = ["A procedure."]

        result = self.dictionary.display_definitions("test", definitions)

        self.assertIn("TEST", result)
        self.assertIn("1. A procedure.", result)

    def test_display_definitions_word_not_found(self):
        result = self.dictionary.display_definitions("xyz", [])
        self.assertIn("not found", result.lower())
        self.assertIn("xyz", result)

    def test_query_definitions_empty_dictionary(self):
        actual_definitions = self.dictionary.query_definitions("test")
        self.assertEqual(actual_definitions, [])
        self.assertFalse(self.dictionary.is_loaded)

    @patch ('driver.FileHandler.write_lines')
    def test_save_query_result_custom_filename(self, mock_write_lines):
     result = "\nTEST\n====\n1. A procedure.\n"
     custom_file = "custom_output.txt"

     self.dictionary.save_query_result(result, custom_file)
     call_args = mock_write_lines.call_args
     self.assertEqual(call_args[0][0], custom_file)







