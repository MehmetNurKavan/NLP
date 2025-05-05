import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re
from collections import Counter

df = pd.read_csv("IMDB Dataset.csv")

# İlk 100 veriyi al (geliştirme için)
df = df.head(100)

documents = df["review"]
labels = df["sentiment"]

# Metin temizleme fonksiyonu
def clean_text(text):
    text = text.lower()  # Küçük harfe çevir
    text = re.sub(r"\d+", "", text)  # Sayıları kaldır
    text = re.sub(r"[^\w\s]", "", text)  # Noktalama işaretlerini kaldır
    text = " ".join([word for word in text.split() if len(word) > 2])  # Kısa kelimeleri çıkar
    return text

# Metinleri temizle
cleaned_documents = [clean_text(doc) for doc in documents]

# CountVectorizer ile BoW (Bag of Words) temsili oluştur
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(cleaned_documents)

# Kelime kümesi
feature_names = vectorizer.get_feature_names_out()

# İlk 2 dokümanın vektör temsili
print("Vector temsili")
vector_temsili_2 = x.toarray()[:2]
print(vector_temsili_2)

# Tüm vektör temsillerinden bir DataFrame oluştur
df_bow = pd.DataFrame(x.toarray(), columns=feature_names)

# Kelime frekansı
word_counts = x.sum(axis=0).A1
word_freq = list(zip(feature_names, word_counts))

# En sık geçen 5 kelime
most_common_words = Counter(dict(word_freq)).most_common(5)
print("En sık geçen 5 kelime:", most_common_words)
