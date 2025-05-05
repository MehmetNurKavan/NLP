# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 15:42:55 2025

@author: Mehmet Nur Kavan
"""
# Kök Bulma (Stemming)

# Kelimeleri köklerine indirger ("running", "ran" → "run").

# Kelimeleri normalleştirerek arama, sınıflandırma, özetleme gibi işlemlerde kullanılır.

import nltk
nltk.download("wordnet")

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["running", "runner", "ran", "better", "go", "went"]
stems = [stemmer.stem(w) for w in words]

print("Stem result:", stem)

# %% lemma

# Daha doğru kök bulma yapar (örn: "went" → "go", "better" → "good").
# Stemming’den daha anlamlı sonuçlar verdiği için daha hassas uygulamalarda kullanılır.


from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# ornek kelime
words = ["running", "runner", "ran", "runs",  "better", "go", "went"]

lemmas = [lemmatizer.lemmatize(w, pos = "v") for w in words]
print("Lemmma result:", lemmas)


'''
"n" (noun)	İsim	cars → car
"v" (verb)	Fiil	running → run
"a" (adjective)	Sıfat	better → good
"r" (adverb)	Zarf	quickly → quick


örnekte de wenti go dieye çevirmiş
'''