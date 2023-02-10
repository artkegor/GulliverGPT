from random import choice, sample
from string import punctuation
from swift import words

book = words


def generate_text():
    global book
    first = list(filter(lambda x: x not in punctuation, book))
    second = ((' '.join((sample(first, choice(range(5, 20)))))).lower()).split()
    for i in second:
        second.insert(0, i[0].upper() + i[1:])
        break
    second.remove(second[1])
    for i in second:
        if second.count(i) != 1:
            del second[' '.join(second).rfind(i)]
    return ' '.join(second) + '.'


def main():
    length = int(input('Сколько строк будет в тексте? '))
    for i in range(length):
        flag = True
        while flag:
            try:
                print(generate_text())
                flag = False
            except IndexError:
                book = words


main()
