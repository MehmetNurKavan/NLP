# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 15:57:07 2025
@author: Mehmet Nur Kavan
"""

# Stop Words (Gereksiz Kelimeleri) Kaldırma

# "ve", "bir", "bu", "is", "the" gibi çok sık kullanılan ama anlam açısından az katkısı olan kelimeleri kaldırıyor.

# Metnin asıl anlamını bozmadan daha kısa ve öz bir metin elde etmek için.

import nltk
from nltk.corpus import stopwords


nltk.download("stopwords")

# İngilizce stopwords listesini yükleme
english_stopwords = set(stopwords.words("english"))

text_english = "This is an example of removing stop words from a text document"

# Stopwords olmayan kelimeleri filtreleme
filtered_english_words = [word for word in text_english.split() if word.lower() not in english_stopwords]

print("Filtered English Words: ", filtered_english_words)

# %% Türkçe stopwords listesini yükleme
try:
    turkish_stopwords = set(stopwords.words("turkish"))
except:
    # Türkçe stopwords listesi yoksa alternatif liste kullan
    turkish_stopwords = set(["ve", "bir", "bu", "ile", "için"])

text_turkish = "merhaba dünya ve güzel insanlar"

# Türkçe metindeki stopwords olmayan kelimeleri filtreleme
filtered_turkish_words = [word for word in text_turkish.split() if word.lower() not in turkish_stopwords]

print("Filtered Turkish Words: ", filtered_turkish_words)

# %% Manuel Türkçe stopwords listesi
custom_turkish_stopwords = set(["ve", "bir", "bu", "ile", "için"])

text_custom_turkish = "Bu bir örnek metin ve stop words'leri temizlemek için kullanılıyor."

# Manuel stopwords listesiyle kelimeleri filtreleme
filtered_custom_turkish_words = [word for word in text_custom_turkish.split() if word.lower() not in custom_turkish_stopwords]

print("Filtered Custom Turkish Words: ", filtered_custom_turkish_words)
