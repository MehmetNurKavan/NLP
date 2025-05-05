#Morphological Analysis (Morfolojik Çözümleme)

import spacy

try:
    # Modeli yükle
    nlp = spacy.load("en_core_web_sm")
    print("Model başarıyla yüklendi!")
except Exception as e:
    print(f"Hata: {e}")

word = "home 47 the Mardin"
doc = nlp(word)

for token in doc:
    print("Text       :", token.text)              # Orijinal kelime
    print("Lemma      :", token.lemma_)            # Kelimenin kökü (örnek: "running" → "run")
    print("POS        :", token.pos_)              # Kelimenin türü (isim, fiil, sıfat vs.)
    print("Tag        :", token.tag_)              # Daha ayrıntılı tür (örn: çoğul isim)
    print("Dependency :", token.dep_)              # Cümledeki görevi (özne, nesne vb.)
    print("Shape      :", token.shape_)            # Kelimenin şekli (örn: "Xxxx", "ddd")
    print("Is alpha   :", token.is_alpha)          # Sadece harf mi?
    print("Is stop    :", token.is_stop)           # Anlamca zayıf, sık kullanılan kelime mi? ("the", "and" gibi)
    print("Morphology :", token.morph)             # Morfolojik özellikler (tekil/çoğul, zaman vb.)
    print(f"Is plural  : {'Number=Plur' in token.morph}")  # Çoğul mu?
    print(" ")
