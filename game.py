from word import Word, colors, capitalize
import getpass
import random
import os

# System call
os.system("")

# Globals
options = ['1', '2']

class languageChoice:
    PORTUGUES = 'src/words/portuguese_words.txt'
    ENGLISH = 'src/words/english_words.txt'


def split(word):
    return [character for character in word]


def randomWord(word_list):
    answer = random.choice(word_list)
    return answer


def isRandomWord():
    choice = str(input("Do you want a random word or type one?\n1) Random\n2) Type\n"))
    
    while choice not in options:
        choice = str(input("Input error! You have to choose between:\n1) Random\n2) Type\n"))


    if choice == '1':
        return True
    else:
        return False
    


def getWordListByLanguage(choice: languageChoice):
    with open(choice, 'r', encoding='utf-8') as file:
        word_list = []
        words = file.readlines()
        for word in words:
            word_list.append(word[:5])

    return word_list


def chooseLanguage():
    choice = str(input("Choose what language you want the words to be:\n1) English\n2) Portuguese\n"))
    
    while choice not in options:
        choice = str(input("Input error! You have to choose between:\n1) English\n2) Portuguese\n"))

    if choice == '1':
        return languageChoice.ENGLISH
    else:
        return languageChoice.PORTUGUES


def chooseWord(word_list: list):
    answer = str(getpass.getpass('Choose a word of five letters ')) # When typing a word, it won't show on the terminal
    while answer not in word_list:
        print("That's not a possible word!")
        answer = str(getpass.getpass('Choose a word of five letters '))

    while len(answer) != 5:
        print("Not enough letters!")
        answer = str(getpass.getpass('Choose a word of five letters '))

    return answer


def attempt(answer, attempts: list, word_list: list):
    attempt = Word(str(input('\nTry a word ')))
    while attempt.word not in word_list:
        print("That's not a possible word!")
        attempt = Word(str(input('\nTry a word ')))

    while len(attempt.word) != 5:
        print("Not enough letters!")
        attempt = Word(str(input('\nTry a word ')))
    attempts.append(attempt)
    
    updateColors(attempt, answer)

    for attempt in attempts:
       attempt.printWord()
       print('\n')

    if attempt.word == answer:
        return True


def updateColors(attempt: Word, answer: str):
    answerCharacters = split(answer)
    characters = split(attempt.word)

    for index in range(5):
        currentAttemptLetter = characters[index]
        currentAnswerLetter = answerCharacters[index]
        
        if currentAttemptLetter == currentAnswerLetter:
            if answer.count(currentAttemptLetter) >= attempt.word.count(currentAttemptLetter):
                attempt.setColor(index, colors.GREEN)
            else:
                if not attempt.firstLetterAlreadyColored(capitalize(currentAttemptLetter)):
                    attempt.setColor(index, colors.GREEN)

        elif currentAttemptLetter in answerCharacters:
            if answer.count(currentAttemptLetter) >= attempt.word.count(currentAttemptLetter):
                attempt.setColor(index, colors.YELLOW)
            else:
                if not attempt.firstLetterAlreadyColored(capitalize(currentAttemptLetter)):
                    biggest_index = answer.find(currentAttemptLetter, index + 1)
                    if attempt.word[biggest_index] == answer[biggest_index]:
                         attempt.setColor(biggest_index, colors.GREEN)
                    else:
                        attempt.setColor(index, colors.YELLOW)

def keepPlaying():
    choice = str(input("Do you want to keep playing?\n1) Yes\n2) No\n"))
    
    while choice not in options:
        choice = str(input("Input error! Do you want to keep playing?\n1) Yes\n2) No\n"))

    if choice == '1':
        return True
    else:
        return False



def round():
    
    word_list = getWordListByLanguage(chooseLanguage())
    attempts = []
    
    if isRandomWord():
        answer = randomWord(word_list)
    else:
        answer = chooseWord(word_list)

    for round in range(6):
        if attempt(answer, attempts, word_list):
            print("You won!")
            break
        elif round == 5:
            print("You lost :'(")
            print("\nThe word was: " + colors.GREEN + "{}".format(answer.upper()) + colors.GREEN)


while True:
    round()
    if not keepPlaying():
        break
