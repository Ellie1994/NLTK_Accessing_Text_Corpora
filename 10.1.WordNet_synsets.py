# WordNet is a semantically-oriented dictionary of English, similar to a traditional thesaurus but with a richer structure. NLTK includes the English WordNet, with 155,287 words and 117,659 synonym sets.

from nltk.corpus import wordnet as wn

print(wn.synsets("lady"))
print()
print(wn.synset("dame.n.02").lemma_names())

# "dame.n.02" is called a synset, or "synonym set", a collection of synonymous words (or "lemmas").
