class Letter:
    def __init__(self, color, letter):
       self.letter = letter
       self.color = color
    
    def __repr__(self):
        return '{} - {}'.format(self.letter, self.color)


class Word:
    def __init__(self, word):
        self.word = word
        self.letters = [Letter('GREY', capitalize(character)) for character in split(word)]

    def setColor(self, index: int, color: str):
        self.letters[index].color = color

    def firstLetterAlreadyColored(self, current_letter):
        for letter in self.letters:
            if letter.letter == current_letter:
                if letter.color != 'GREY':
                    return True

    def printWord(self):
        return print(self.letters)


def capitalize(character: str):
    return character.upper()


def split(word):
    return [character for character in word]

