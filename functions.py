import word

def split(word):
    return [character for character in word]


def chooseWord():
    answer = str(input('Choose a word of five letters'))
    while len(answer) != 5:
        print("The word has to be five lettered.")
        answer = str(input('Choose a word of five letters'))

    return answer


def attempt(answer):
    attempt = word.Word(str(input('Try a word')))
    while len(attempt.word) != 5:
        print("The word has to be five lettered.")
        attempt = word.Word(str(input('Try a word')))

    if attempt == answer:
        return True
    
    updateColors(attempt, answer)


def updateColors(attempt: word.Word, answer: str):
    answerCharacters = split(answer)
    characters = split(attempt.word)

    for index in range(5):
        currentAttemptLetter = characters[index]
        currentAnswerLetter = answerCharacters[index]
        
        if currentAttemptLetter == currentAnswerLetter:
            if not attempt.firstLetterAlreadyColored(word.capitalize(currentAttemptLetter)) :
                attempt.setColor(index, 'GREEN')

        elif currentAttemptLetter in answerCharacters:
            if answer.count(currentAttemptLetter) >= attempt.word.count(currentAttemptLetter):
                attempt.setColor(index, 'YELLOW')
            else:
                if not attempt.firstLetterAlreadyColored(word.capitalize(currentAttemptLetter)):
                    attempt.setColor(index, 'YELLOW')

    return attempt.printWord()


def round():
    answer = chooseWord()
    for round in range(6):
        if attempt(answer):
            print("You won!")
            break
        elif round == 5:
            print("You lost :'(")
round()