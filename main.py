import random
import string
def menu():
    print("Type \"play\" to play the game, \"exit\" to quit: ")
    return input()
def main_module():
    repeated_letters = []
    list_of_words = ['python', 'java', 'kotlin', 'javascript']
    word_selected =  random.choice(list_of_words)
    dashes = '-' * ((len(word_selected)))
    temp = list(dashes)
    print("H A N G M A N")
    mistakes = 8
    while mistakes > 0:
        i = 0
        if word_selected == dashes:
                print("You survived!")
                break
        print()
        print(dashes)
        letter = (input("Input a letter: "))
        if len(letter) > 1:
            print("You should input a single letter")
        elif letter not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
        elif letter in repeated_letters:
            print("You've already guessed this letter")
            repeated_letters.append(letter)
        elif letter in dashes:
            print("You've already guessed this letter")
            repeated_letters.append(letter)
        elif letter not in word_selected:
            print("That letter doesn't appear in the word")
            repeated_letters.append(letter)
            mistakes = mistakes - 1
            if mistakes ==0:
                print('You lost!')
        else:
            for j in word_selected:
                if letter == j:
                    temp[i] = letter
                i = i + 1
            dashes = "".join(temp)
            if word_selected == dashes:
                print("You guessed the word",dashes,"!")
                print("You survived!")
                break
while menu() == 'play':
    main_module()
