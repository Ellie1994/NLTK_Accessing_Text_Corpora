# hier you see a one-pair dictionary with the language combination German to Englisch and vice a versa:

from nltk.corpus import swadesh


de_to_en = swadesh.entries(["de", "en"])      
en_to_de = swadesh.entries(["en", "de"])


translate = dict(de_to_en)
translate1 = dict(en_to_de)

translate.update(dict(translate1))


print(translate["Hund"]) 
print(translate["dog"])
