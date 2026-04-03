"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = [",", "*", ";", ".", ":","(", "[", "]", ")"]

    def __init__(self):
        self.text = None
        self.word_count = {}

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = book_file.readlines()

        #strip out empty lines
        stripped_text = []
        for line in self.text:
            if line != "\n":
                stripped_text.append(line)
        self.text = stripped_text

        # convert list of lines to list of words
        words = []
        for line in self.text:
            words += line.split()
        self.text = words

        # remove common punctuation from words
        temp_text = []
        for word in self.text:
            temp_word = word
            for punctuation in self.COMMON_PUNCTUATION:
                temp_word = temp_word.replace(punctuation, '')
            temp_text.append(temp_word)
        self.text = temp_text

        for word in self.text:
            lower_word = word.lower()
            self.word_count[lower_word] = self.word_count.get(lower_word, 0) + 1



    """
    Checks to see if the given word appears in the provided sequence.
    This check is case in-sensitive.
    :param word: a string
    :param word_list: a sequence of words
    :return: True if not found, false otherwise
    """

    @staticmethod
    def is_unique(word, word_list):
        for a_word in word_list:
            if word == a_word:  # no .lower() needed anymore!
                return False
        return True


    def find_unique_words(self):
        """
        Filters out all the words in the text.
        :return: a list of all the unique words.
        """
        # Just loops through the dictionary once and returns words where count == 1, O(N)!

        # return [word for word, count in self.word_count.items() if count == 1]

        # should return words from self.txt(original casting), just uses dict to
        # check if count==1
        return [word for word in self.text
                if self.word_count[word.lower()] == 1]


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("-"*50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-"*50)
    for word in unique_words:
        print(word)
    print("-"*50)


if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')