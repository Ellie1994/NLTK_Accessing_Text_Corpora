# If you have your own collection of text files that you would like to access, you can load them with the help of NLTK's PlaintextCorpusReader. 

import nltk
from nltk.corpus import PlaintextCorpusReader

corpus_root = "NLTK" # name of a directory

word_list = PlaintextCorpusReader(corpus_root, ".*") # The second parameter of the PlaintextCorpusReader initializer can be a list of fileids, like ['a.txt', 'test/b.txt'] or a pattern that matches all fileids like '[abc]/.*\.txt' 

print(word_list.fileids())

print(word_list.words("5.statistics.py")) # name of a file
