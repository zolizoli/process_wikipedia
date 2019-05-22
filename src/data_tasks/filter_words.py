with open('data/interim/vocabulary.tsv', 'r') as dictfile:
    vocabulary = set()
    for line in dictfile:
        wd, freq = line.strip().split('\t')
        if int(freq) > 50 and len(wd) > 1:
            vocabulary.add(wd.strip())
print(len(vocabulary))
with open('data/interim/full_text_wiki.txt', 'r') as infile:
    with open('data/processed/filtered_wiki.txt', 'w') as outfile:
        for line in infile:
            line = line.strip().split()
            lineset = set(line)
            wordintersect = vocabulary.intersection(lineset)
            line = [wd for wd in line if wd in wordintersect]
            line = ' '.join(line) + '\n'
            outfile.write(line)
