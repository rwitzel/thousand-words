import re

with open('thousand_words.txt') as f:
    word_contents = f.read()

#print(word_contents)
words = re.split(r'[\s,.]+', word_contents)
print(words)