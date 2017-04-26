"""
@ilya-besancon
Analyzes the word frequencies in a book downloaded from
Project Gutenberg.
In this case, I look at Martin Eden.
"""

import re


def get_word_list(file_name, n):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    # read file:
    book = open(file_name, 'r')
    allwords = book.read()
    # return as list of words:
    word_list = re.compile('\w+').findall(allwords)
    # makes all words lowercase
    word_list = [str.lower(word) for word in word_list]
    # print('Testing full list: ', word_list[:150])
    return get_top_n_words(word_list, n)


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequently occurring
    """
    # initializing dictionary and lists of words and their frequencies
    d = dict()
    words = []

    # adds one of each word to list
    for word in word_list:
        if word not in words:
            words.append(word)
    # adds count of each word to a dictionary
    for word in word_list:
        count = d.get(word, 0)
        d[word] = count + 1
    # reverse key/values of dictionary
    new_dict = {y: x for x, y in d.items()}
    # sort by highest to lowest count
    keys = sorted(new_dict.keys())
    # make a list of most frequent n words
    order_words = []
    for key in keys:
        order_words.append(new_dict.get(key))
    order_words = order_words[::-1]
    order_words = order_words[:n]
    return order_words


if __name__ == "__main__":
    print("Running WordFrequency Toolbox. This might take a second.")
    # number of top words:
    n = 10
    result = get_word_list('martineden.txt', n)
    print("Top ", n, 'words: ', result)
    print("Wouldn't you think the author might be more creative? Joking!")
