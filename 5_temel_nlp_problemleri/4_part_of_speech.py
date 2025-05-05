# cümlelerdeki her kelimenin (token) Part-of-Speech (POS) yani sözcük türünü (isim, fiil, sıfat vb.) tespit eder.

import spacy

try:
    # Modeli yükle
    nlp = spacy.load("en_core_web_sm")
    print("Model başarıyla yüklendi!")
except Exception as e:
    print(f"Hata: {e}")

sentence1 = "What is the weather like today"

# Cümle doğal dil işlemeye gönderiliyor
doc1 = nlp(sentence1)

# Her bir kelime (token) için, sözcük türü ekrana yazdırılıyor
print("Sentence 1 POS Tags:")
for token in doc1:
    print(token.text, token.pos_)

print("\n")

sentence2 = "I went to the store, but they were closed, so I had to go to another store"

# İkinci cümle de işleniyor
doc2 = nlp(sentence2)

# Her bir kelime için, sözcük türü yazdırılıyor
print("Sentence 2 POS Tags:")
for token in doc2:
    print(token.text, token.pos_)
