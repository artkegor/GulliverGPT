from string import punctuation
from random import choice
from swift import words

global book
book = words

# Here I remove all punctuation marks from the book
# Process is very long.
for i in range(len(book)):
    if book[i] in punctuation:
        book[i] = ''
for i in range(book.count('')):
    book.remove('')


def get_first_word():
    # Here I choose a random word from the book and check if it not a punctuation mark
    first_word = ''
    while first_word in punctuation:
        first_word = choice(words)
    return first_word.capitalize()


def get_next_word(current_word):
    # Here I create a list of indexes of the current word in the book
    # If the list is empty, I return a random word from the book
    # If the list is not empty, I choose a random index from the list
    # If the index is the last in the book, I return a random word from the book
    # If the index is not the last in the book, I return the next word in the book
    indexes = []
    for i in range(len(book)):
        if book[i] == current_word:
            indexes.append(i)
    if len(indexes) == 0:
        return choice(book)
    index = choice(indexes)
    if index == len(book) - 1:
        return choice(book)
    else:
        next_word = book[index + 1]
    return next_word.lower()


def get_sentence(length):
    # Here I create a list of words and add the first word to it
    # Then I add the next word to the list until the list is the desired length
    sentence = [get_first_word()]
    for i in range(length - 1):
        sentence.append(get_next_word(sentence[-1]))
    return ' '.join(sentence)


def main():
    # Here I ask the user for the desired length and number of sentences
    length = int(input('Enter the desired length of the sentence: '))
    number = int(input('Enter the desired number of sentences: '))
    for i in range(number):
        print(get_sentence(length) + '.')


if __name__ == '__main__':
    main()
