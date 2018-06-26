# The Brown Corpus was the first million-word electronic corpus in English, created in 1961 at Brown University. This corpus contains text from 500 sources, and the sources have been categorized by genre, such as news, editorial, and so on(for a complete genre-list, see http://icame.uib.no/brown/bcm-los.html).

import nltk
from nltk.corpus import brown

print(brown.categories())
print()

print(brown.words(categories="humor"))
print()

print(brown.words(fileids=["ch15"]))
print()

print(brown.sents(categories=["mystery","science_fiction", "adventure"]))
