# The Names corpus, contains 8.000 first names categorized by gender. The male and female names are stored in separate files. Let's find names which appear in both files.

import nltk

names = nltk.corpus.names
print(names.fileids())
# output: '['female.txt', 'male.txt']'

male = names.words('male.txt')
female = names.words('female.txt')

same = [w for w in male if w in female]

print(same)
