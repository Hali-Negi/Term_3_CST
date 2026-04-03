# Group 9

# Name: Kai Steingarten
# Student number: A01435070

# Name: Hali Imanpanah
# Student number: A01424306

# Name: Anna Jang
# Student number: A01405877

from pathlib import Path
from file_handler import FileHandler, FileExtensions, InvalidFileTypeError, FileEnumMismatchError


class Dictionary:
    """
    A dictionary class that loads word definitions from files and allows querying.
    """

    def __init__(self):

        """
        Initialize the Dictionary with empty data and tracking attributes.
        """

        self.data ={}  # Stores word: [list of definitions]
        self.is_loaded = False # Track if dictionary has been loaded
        self.query_history = []

    def load_dictionary(self, filepath):
        """
        Load dictionary data from a file (.json or .txt).
        """
        # Create a Path object to work with the file
        file_path = Path(filepath)
        extension = file_path.suffix[1:]

        try:
            file_enum = FileExtensions(extension)
        except ValueError as e:
            raise InvalidFileTypeError(extension) from e
        else:
            # Use FileHandler to load the data, it returns a dictionary
            self.data = FileHandler.load_data(filepath, file_enum)
            self.is_loaded = True


    def query_definitions(self, word: str):

        """
        Query the definitions of a word (case-insensitive).
        """

        # Make the search case-insensitive
        word_lower = word.casefold()

        try:
            definitions = self.data[word_lower]
        except KeyError:
            return []
        else:
            self.query_history.append((word, definitions))
            return definitions

    def display_definitions(self, word, definitions):

            if not definitions:
                return f"'{word}' not found in the dictionary"

            # Format the output
            result = f"\n{word.upper()}:\n"
            result += "=" * len(word) + "\n"

            for i, definitions in enumerate(definitions, 1):
                result += f"{i}. {definitions}\n"

            return result

    def save_query_result(self, result, output_file = "query_history.txt"):
        """
        Save the query result to text file.
        """

        # Split result into lines for writing
        lines = result.strip().split('\n')

        # Use FileHandler to write lines to file
        FileHandler.write_lines(output_file, lines)


def main():

    """
    Main driver function for the dictionary program.
    Loads the dictionary and allows users to query word definitions.
    """
    print("=" * 50)
    print("Welcome to the MIDI Dictionary")
    print("=" * 50)

    # Create a Dictionary object
    dictionary = Dictionary()

    try:
        print("Loading dictionary...")
        dictionary.load_dictionary("data.json")
        print(" Dictionary loaded successfully!")
        print(f"Total words: {len(dictionary.data)}")

    except FileNotFoundError:
        print("✗ Error: data.json file not found!")
        return

    except InvalidFileTypeError as e:
        print(f"✗ Error: {e}")
        return

    except FileEnumMismatchError as e:
        print(f"✗ Error loading dictionary: {e}")
        return

    # Main query loop
    print("\n" + "=" * 50)
    print("You can now search for word definitions!")
    print("Type 'exit program' to quit.")
    print("=" * 50)

    while True:
        # Get user input
        user_input = input("\nEnter a word to search: ").strip()

        if user_input.lower() == "exit program":
            print("Thank you for using the Dictionary Program!")
            print("Goodbye")
            break

        # Skip empty input
        if not user_input:
            print("Please enter a word.")
            continue

        # Query the definition
        try:
            definitions = dictionary.query_definitions(user_input)

            # Display the result
            result = dictionary.display_definitions(user_input, definitions)
            print(result)

            # Save the query result to file
            if definitions:  # Only save if word was found
                dictionary.save_query_result(result)

        except InvalidFileTypeError as e:
            print(f"An error occurred while writing query history: {e}")


if __name__ == '__main__':
    main()