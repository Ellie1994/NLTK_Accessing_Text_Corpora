# We can make this simple translator more useful by adding other source languages. Let's get the German-English and Russian-English pairs: we convert each to a dictionary using dict(), then update our original translate dictionary with these additional mappings.

from nltk.corpus import swadesh


de_to_en = swadesh.entries(['de', 'en'])    
ru_to_en = swadesh.entries(['ru', 'en'])  

translate = dict(de_to_en)
translate1 = dict(ru_to_en)

translate.update(dict(translate1))


print(translate["Hund"])
print(translate["человек"])
print(translate["fliegen"])
print(translate["плохой"])
