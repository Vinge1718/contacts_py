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
    with open(text_file, "r") as handle:
        data = handle.read().split()
        counter = 0
        for word in data:
            if word == key:
                counter += 1
    return counter

def count_lines(text_file):
    """
    Function that counts the number of lines in a file
    """
    with open(text_file, "r") as handle:
        data = handle.readlines()
        counter = 0
        for line in data:
            counter+=1

        return counter

def long_string(text_file):
    """
    Function trhat returns the longest string in a document
    """
    with open(text_file, "r") as handle:
        data = handle.read().split()
        string = max(data, key=len)
        return len(string)