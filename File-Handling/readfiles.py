text_file = "test.txt"
def read_file(text_file):
    """
    Function that reads a text file and returns the data from the text file

    Raises:
        FileNotFoundError: If it cannot find the file 
    """
    try:
        with open(text_file, "r") as handle:
            data = handle.read()
            return data

    except FileNotFoundError:
        return None

def count_words(key):
    """
    Function that takes in a word and counts the number of times the word occurs in a text
    """
    with open("test.txt", "r") as handle:
        data = handle.read().split()
        counter = 0
        for word in data:
            if word == key:
                counter += 1
    return counter
