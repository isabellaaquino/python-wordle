class Letter:
    def __init__(self, color, letter):
       self.color = color
       self.letter = letter
    
    def __repr__(self):
        return '{} - {}'.format(self.letter, self.color)


class Word:
    def __init__(self, word):
        self.word = word
        self.greens = 0
        self.letters = [Letter('GREY', capitalize(character)) for character in split(word)]

    def setColor(self, letter, color):
        for letters in self.letters:
            if letters.letter == letter:
                letters.color = color

    def printWord(self):
        return print(self.letters)

    def allGreen(self):
        if self.greens == 5:
            return True
        else:
            return False


def capitalize(character: str):
    return character.upper()


def split(word):
    return [character for character in word]

