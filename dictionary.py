"""
Speller.py
Spell check python script

1/13/2019

Chandira Withanage

"""
words = set()


def check(word):
    return word.lower() in words


def load(dictionary):
    with open(dictionary, "r") as file:
        for line in file:
            words.add(line.rstrip("\n"))
            pass
    return True


def size():
    return len(words)


def unload():
    return True
