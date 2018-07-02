# It is also useful to knoe how we can compare words in various languages.

from nltk.corpus import swadesh

languages = ["la", "it", "fr", "en"]
for word in [100, 101, 102, 103]:
    print(swadesh.entries(languages)[word])

# output:
# ('videre', 'vedere', 'voir', 'see')
# ('audire', 'udire, sentire', 'entendre', 'hear')
# ('scire', 'sapere', 'savoir', 'know (a fact)')
# ('putare', 'pensare', 'penser', 'think')
