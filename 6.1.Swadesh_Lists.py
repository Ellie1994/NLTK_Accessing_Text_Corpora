# An example of a tabular lexicon is the comparative wordlist. NLTK includes so-called Swadesh wordlists, lists of about 200 common words in several languages. The Swadesh list is used in the quantitative assessment of the genealogical relatedness of languages. 

from nltk.corpus import swadesh

print(swadesh.fileids()) 

# prints out the language identifiers (two-letter code).
print() # prints out an empty line.

print(swadesh.words("de"))

# prints out 200 common German words from swadesh.
