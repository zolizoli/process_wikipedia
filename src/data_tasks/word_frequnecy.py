from collections import Counter

word_freq = Counter([])
with open('data/interim/full_text_wiki.txt', 'r') as infile:
    for line in infile:
        line = line.strip().split()
        word_freq.update(Counter(line))

with open('data/interim/vocabulary.tsv', 'w') as outfile:
    for k,v in word_freq.items():
        o = k + '\t' + str(v) + '\n'
        outfile.write(o)
