# Algorithm used to obtain all 5-letter words in english

with open('all_words.txt', 'r', encoding='utf-8') as file, open('english_words.txt', 'w', encoding='utf-8') as f2:
    unconverted_lines = file.readlines()
    for line in unconverted_lines:
        if len(line) == 6 and line.find('.') == -1 and not line[0].isupper():
            f2.write(line)
