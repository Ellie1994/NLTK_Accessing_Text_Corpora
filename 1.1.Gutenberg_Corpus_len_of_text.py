# 1. Gutenberg Corpus

# NLTK includes a small selection of texts from the Project Gutenberg electronic text archive, which contains 25,000 free electronic books, hosted at http://www.gutenberg.org/. We begin by getting the Python interpreter to load the NLTK package, then ask to see nltk.corpus.gutenberg.fileids(), the file identifiers in this corpus: #


import nltk 
file_ids = nltk.corpus.gutenberg.fileids()

print(file_ids)

print()# prints out a blank raw
##############################################

hamlet = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
print("the total amount of words in 'shakespeare-hamlet.txt': " + str(len(hamlet)))

# prints out how many words it contains
