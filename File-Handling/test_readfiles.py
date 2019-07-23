import unittest
import readfiles

class TestReadFiles(unittest.TestCase):
    """
    Class to test the functions on the readfiles module
    Args:
        unittest.TestCase: Class from the unittest module to create unit tests
    """

    def test_get_data(self):
        """
        Test case to confirm that we are getting data from the file
        """

        with open("test.txt", "r") as handle:
            data = handle.read()
            self.assertEqual(data, readfiles.read_file("test.txt"))

    def test_nonfile(self):
        """
        Test to confirm that an exeption is raised when a wrong file is inputted
        """
        self.assertEqual(None, readfiles.read_file("tests.txt"))

    def test_word_count(self):
        """
        Test to count the number of times the word "Ipsum" has been used
        """

        with open("test.txt", "r") as handle:
            data = handle.read().split()
            count = 0
            for word in data:
                if word == "Ipsum":
                    count+=1
        self.assertEqual(count, readfiles.count_words("Ipsum"))

    def test_line_count(self):
        """
        Test to count how many lines we have in a text document
        """
        with open("test.txt", "r") as handle:
            data = handle.readlines()
            connt = 0
            for line in data:
                connt +=1
        self.assertEqual(connt, readfiles.count_lines("test.txt"))

    def test_longest_word(self):
        """
        Test to check for the longest word in the document
        """
        with open("test.txt", "r") as handle:
            data = handle.read().split()
            longest_string = max(data, key=len)
            self.assertEqual(len(longest_string), readfiles.long_string("test.txt"))

if __name__ == "__main__":
    unittest.main()

