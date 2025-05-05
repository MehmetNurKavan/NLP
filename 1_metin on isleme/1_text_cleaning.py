# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 14:48:39 2025

@author: Mehmet Nur Kavan
"""

# metinlerdeki fazla boşlukları temizleme

text1 = "Hello,      World!    2047" # "Hello, World! 2047
text1.split()
cleaned_text1 = " ".join(text1.split())

print(cleaned_text1)

# %% buyuk -< kucuk harf ceviri

text2 = "Hello, World! 2047"
cleaned_text2 = text2.lower()
print(cleaned_text2)

# %% noktalama isaretlerini kaldir

import string

text3 = "Hello, World! 2047"
cleaned_text3 = text3.translate(str.maketrans("", "", string.punctuation))
print(cleaned_text3)

# %% ozel karakterileri kaldır

import re

text4 = "Hello, World! 2047"
cleaned_text4 = re.sub(r"[^A-Za-z0-9\s]","", text4)
print(cleaned_text4)

# %% yazim hatalarini duzelt

from textblob import TextBlob

text5_with_errors = "Helıo, Wirld! 2047"
cleaned_text5 = str(TextBlob(text5_with_errors).correct())
print(cleaned_text5)

# %% html etiketleriini kaldirilasi

from bs4 import BeautifulSoup

text6_html = "<div>Hello, World! 2047</div>"
cleaned_text6 = BeautifulSoup(text6_html, "html.parser").get_text()
print(cleaned_text6)

