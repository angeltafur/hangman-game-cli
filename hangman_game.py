#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: Angel Tafur
"""

from os import system
from time import sleep
from random import choice as random_word

PARTS_HANGMAN = ['''





         ''', '''





=========''', '''  +
  |
  |
  |
  |
  |
=========''', '''  +---+
  |
  |
  |
  |
  |
=========''', '''  +---+
  |   |
  |
  |
  |
  |
=========''', '''  +---+
  |/  |
  |
  |
  |
  |
=========''', '''  +---+
  |/  |
  |   O
  |
  |
  |
=========''', '''  +---+
  |/  |
  |   O
  |   |
  |
  |
=========''', '''  +---+
  |/  |
  |   O
  |   |\\
  |
  |
=========''', '''  +---+
  |/  |
  |   O
  |  /|\\
  |
  |
=========''', '''  +---+
  |/  |
  |   O
  |  /|\\
  |    \\
  |
=========''', '''  +---+
  |/  |
  |   O
  |  /|\\
  |  / \\
  |
=========''']


TITLE = """\t█░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█    █▀▀ ▄▀█ █▀▄▀█ █▀▀
\t█▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█    █▄█ █▀█ █░▀░█ ██▄
\t===============================    =================
"""


WIN = """
 ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗██╗   ██╗██╗      █████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██║     ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ██║   ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║███████╗
██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ██║   ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
"""


LOSE = """
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
"""


BYE = """▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ██ ██ ▀██ █▄▄ ▄▄█▄ ▄██ ███████ ▀██ ██ ▄▄▄█▄▀█▀▄█▄▄ ▄▄███▄▄ ▄▄█▄ ▄██ ▄▀▄ ██ ▄▄▄
██ ██ ██ █ █ ███ ████ ███ ███████ █ █ ██ ▄▄▄███ █████ ███████ ████ ███ █ █ ██ ▄▄▄
██▄▀▀▄██ ██▄ ███ ███▀ ▀██ ▀▀ ████ ██▄ ██ ▀▀▀█▀▄█▄▀███ ███████ ███▀ ▀██ ███ ██ ▀▀▀
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
"""


def read():
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        words = [word for word in f]
    return random_word(words).replace("\n", "")


def normalize(word):
    replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    for a, b in replacements:
        word = word.replace(a, b)
    return word


def header(c, underscores):
    system("clear")
    print(TITLE)
    print("GUESS THE WORD!\n")
    print(PARTS_HANGMAN[c])
    print("\nHidden Word: " + underscores + "\n")


def main():
    flag = True
    while flag:
        keyword = read()
        normalize_word = normalize(keyword)
        underscores = "_" * len(keyword)
        c = 0
        header(c, underscores)
        while c < (len(PARTS_HANGMAN) - 1) and "_" in underscores:
            try:
                letter = input("Enter a letter: ")
                if len(letter) == 1 and not letter.isalpha():
                    raise ValueError("\nShouldn't enter a character other than a letter!\n")
                elif len(letter) > 1 or len(letter) == 0:
                    raise ValueError("\nPlease must enter one letter!\n")
                if letter in normalize_word:
                    indexes = [i for i, e in enumerate(normalize_word) if letter == e]
                    for index in indexes:
                        underscores = underscores[:index] + keyword[index].upper() + underscores[index + 1:]
                    header(c, underscores)
                    if not "_" in underscores:
                        system("clear")
                        print(WIN)
                else:
                    c += 1
                    header(c, underscores)
            except ValueError as ve:
                print(ve)
                input("Press Enter key to continue...")
                header(c, underscores)
        if c == len(PARTS_HANGMAN) - 1:
            system("clear")
            print(LOSE)
            print("The hidden word was: " + keyword.upper() + "\n" )
        option = input("Do you want to keep playing? Enter any key(continue) / N(quit): ")
        if option == 'n' or option == "N":
            flag = False
    system("clear")
    print(BYE)
    sleep(1)
    system("clear")


if __name__ == "__main__":
    main()