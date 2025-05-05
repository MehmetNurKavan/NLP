# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 15:21:08 2025

@author: Mehmet Nur Kavan
"""

# Tokenization (Kelimelere ve Cümlelere Ayırma)
# Metni parçalara bölüp analiz yapmak için temel adımdır. Örneğin: duygusal analiz, metin özetleme.

''' Nerede işine yarar?
Metni parçalara bölüp analiz yapmak için temel adımdır. Örneğin: duygusal analiz, metin özetleme.'''
import nltk

nltk.download("punkt")

text = "Hello, World! How Are You?"

# kelimeleri tokenlere ayır
word_tokens = nltk.word_tokenize(text)

# cumle tokenizasyonu
sentence_tokens = nltk.sent_tokenize(text)

print("Kelime Tokenleri:", word_tokens)
print("Cümle Tokenleri:", sentence_tokens)

'''
beklenile çıktı:
Kelime Tokenleri: ['Hello', ',', 'World', '!', 'How', 'Are', 'You', '?']
Cümle Tokenleri: ['Hello, World!', 'How Are You?']
'''