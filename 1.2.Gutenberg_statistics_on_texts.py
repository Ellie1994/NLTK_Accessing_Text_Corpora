from nltk.corpus import gutenberg
for w in gutenberg.fileids():
    print(w)


for files in gutenberg.fileids():
    num_char = len(gutenberg.raw(files))
    num_words = len(gutenberg.words(files))
    num_sents = len(gutenberg.sents(files))
    num_vocab = len(set(w.lower() for w in gutenberg.words(files)))

    print(round(num_char/num_words), round(num_words/num_sents), round(num_words/num_vocab), files)

# ctrl + s = stop
# ctrl + q = continue 
# ctrl + c = cansel 
