class colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    GREY = '\033[0m'
    BOLD = '\033[1m'

class Letter:
    def __init__(self, color: colors, letter):
       self.letter = letter
       self.color = color
    
    def __repr__(self):
        return '{} - {}'.format(self.letter, self.color)


class Word:
    def __init__(self, word):
        self.word = word
        self.letters = [Letter(colors.GREY, capitalize(character)) for character in split(word)]

    def setColor(self, index: int, color: colors):
        self.letters[index].color = color

    def firstLetterAlreadyColored(self, current_letter):
        for letter in self.letters:
            if letter.letter == current_letter:
                if letter.color != colors.GREY:
                    return True
                else:
                    return False

    def printWord(self):
        for letter in self.letters:
            print(colors.BOLD + letter.color + letter.letter + letter.color + colors.BOLD, end=' ')


def capitalize(character: str):
    return character.upper()


def split(word):
    return [character for character in word]

