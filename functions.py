import word

def split(word):
    return [character for character in word]


def chooseWord():
    answer = str(input('Choose a word up to five letters'))
    while len(answer) != 5:
        print("The word has to be five letters.")
        answer = str(input())

    return answer


def attempt(answer):
    attempt = word.Word(str(input('Try a word')))
    while len(attempt.word) != 5:
        print("The word has to be five letters.")
        attempt = word.Word(str(input('Try a word')))
    
    updateColors(attempt, answer)
    
    return attempt.allGreen()


def updateColors(attempt: word.Word, answer):
    answerCharacters = split(answer)
    characters = split(attempt.word)

    for index in range(5):
        letra_atual = characters[index]
        letra_atual_resposta = answerCharacters[index]
        if letra_atual == letra_atual_resposta:
            attempt.setColor(word.capitalize(letra_atual), 'GREEN')
            attempt.greens+=1

        elif letra_atual in answerCharacters:
            attempt.setColor(word.capitalize(letra_atual), 'YELLOW')

    if not attempt.allGreen:
        attempt.greens = 0

    return attempt.printWord()


def round():
    answer = chooseWord()
    for round in range(6):
        if attempt(answer):
            return print("You won!")
    print("You lost.")
round()