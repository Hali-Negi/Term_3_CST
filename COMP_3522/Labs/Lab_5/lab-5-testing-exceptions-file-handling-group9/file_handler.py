import json
import pathlib
from enum import StrEnum, auto


class InvalidFileTypeError(ValueError):
    """Raised when an invalid file type is provided."""


class FileEnumMismatchError(ValueError):
    """Raised when the file type is provided does not match the file_extension_enum provided."""

    def __init__(self, path, file_extension_enum):
        super().__init__(f"Provided path ({path}) does not match provided file_extension_enum "
                         f"{file_extension_enum}.")


class FileExtensions(StrEnum):
    """Valid file extensions."""
    TXT = auto()
    JSON = auto()


class FileHandler:

    @staticmethod
    def load_data(path, file_extension_enum):
        """Load data from a .json or .txt file.

        :raises InvalidFileTypeError: if path is not a .txt or .json file
        :raises FileNotFoundError: if no file exists at path
        :raises FileEnumMismatchError: if file_extension_enum does not match path file extension
        """
        file_path = pathlib.Path(path)
        suffix = file_path.suffix.lstrip(".")
        if suffix not in FileExtensions:
            raise InvalidFileTypeError(f"{suffix} is not a valid file extension. "
                                       f"Please provide a .txt or .json file.")

        if not path.endswith(file_extension_enum):
            raise FileEnumMismatchError(path, file_extension_enum)

        if not file_path.exists():
            raise FileNotFoundError(f"File {path} does not exist.")

        with open(file_path, mode="r", encoding="utf-8") as data_file:
            if file_extension_enum == FileExtensions.JSON:
                return json.load(data_file)
            else:
                lines = data_file.readlines()
                return FileHandler._parse_dictionary_from_text(lines)

    @staticmethod
    def write_lines(path, lines):
        """
        Appends a list of strings to a specified text file line by line.

        :raises InvalidFileTypeError: if path is not a .txt
        """
        file_path = pathlib.Path(path)
        if file_path.suffix.lstrip(".") != FileExtensions.TXT:
            raise InvalidFileTypeError(f"Path must be a .txt file. {file_path} is not a .txt file.")

        with open(path, mode="a", encoding="utf-8") as text_file:
            for line in lines:
                if not line.endswith("\n"):
                    with_new_line = "".join([line, "\n"])
                text_file.write(with_new_line)

    @staticmethod
    def _parse_dictionary_from_text(file_lines):
        dictionary = {}
        word = ""
        definitions = []
        for line in file_lines:
            if not line.startswith("="):
                if line[0].isdigit():
                    definition = line.split(" ", maxsplit=1)[-1].strip()
                    definitions.append(definition)
                elif line[0].isalpha():
                    if word:
                        dictionary[word] = definitions
                    word = line.strip(":\n").casefold()
                    definitions = []
        dictionary[word] = definitions
        return dictionary
