import json
import nltk
import string
from smart_open import smart_open

filter = ['...', "''", '``']


def clean_word(wd):
    fcharacter = wd[0]
    echaracter = wd[-1]
    if not fcharacter.isalnum():
        wd = wd[1:]
    if not echaracter.isalnum():
        wd = wd[:-1]
    return wd


with open('data/interim/full_text_wiki.txt', 'w') as outfile:
    for line in smart_open('data/raw/enwiki-latest.json'):
        article = json.loads(line)
        texts = article['section_texts']
        for text in texts:
            text = text.replace('=', '')
            text = text.replace("''", '')
            text = text.replace("``", '')
            sentences = nltk.sent_tokenize(text, 'english')
            for sentence in sentences:
                words = nltk.word_tokenize(sentence, 'english')
                words = [clean_word(wd.lower()) for wd in words
                         if wd not in string.punctuation
                         and wd not in filter]
                if len(words) > 0:
                    sent = ' '.join(words) + '\n'
                    outfile.write(sent)
