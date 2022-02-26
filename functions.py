import word

def split(word):
    return [character for character in word]


def chooseWord():
    answer = str(input('Choose a word up to five letters'))
    while len(answer) != 5:
        print("The word has to be five letters.")
        answer = str(input('Choose a word up to five letters'))

    return answer


def attempt(answer):
    attempt = word.Word(str(input('Try a word')))
    while len(attempt.word) != 5:
        print("The word has to be five letters.")
        attempt = word.Word(str(input('Try a word')))

    if attempt == answer:
        return True
    
    updateColors(attempt, answer)


def updateColors(attempt: word.Word, answer: str):
    answerCharacters = split(answer)
    characters = split(attempt.word)

    for index in range(5):
        letra_atual = characters[index]
        letra_atual_resposta = answerCharacters[index]
        
        if letra_atual == letra_atual_resposta:
            if not attempt.firstLetterAlreadyColored(word.capitalize(letra_atual)) :
                attempt.setColor(index, 'GREEN')

        elif letra_atual in answerCharacters:
            if answer.count(letra_atual) >= attempt.word.count(letra_atual):
                attempt.setColor(index, 'YELLOW')
            else:
                if not attempt.firstLetterAlreadyColored(word.capitalize(letra_atual)):
                    attempt.setColor(index, 'YELLOW')

    return attempt.printWord()


def round():
    answer = chooseWord()
    for round in range(6):
        if attempt(answer):
            break
        if round == 5:
            print("You lost")
round()