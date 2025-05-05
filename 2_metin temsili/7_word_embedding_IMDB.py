import pandas as pd
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import re

df = pd.read_csv("IMDB Dataset.csv")
print(df.head(10))

documents = df["review"]  # Sadece yorumlar alınır

# Metin temizleme fonksiyonu
def clean_text(text):
    text = text.lower()  # Küçük harfe çevir
    text = re.sub(r"\d+", "", text)  # Sayıları temizle
    text = re.sub(r"[^\w\s]", "", text)  # Noktalama ve özel karakterleri temizle
    text = " ".join([word for word in text.split() if len(word) > 2])  # 2 harf ve altındaki kelimeleri çıkar
    return text

# Tüm belgeleri temizle
cleaned_documents = [clean_text(doc) for doc in documents]

# Cümleleri tokenize et
tokenized_documents = [simple_preprocess(doc) for doc in cleaned_documents]

# Word2Vec modeli oluşturuluyor
# sg=1: Skip-gram algoritması kullanılır (genellikle düşük veriyle daha iyi sonuç verir)
model = Word2Vec(sentences=tokenized_documents, vector_size=50, window=5, min_count=1, sg=1)

# Modelden kelime vektörlerini al
word_vectors = model.wv
words = list(word_vectors.index_to_key)[:500]  # En sık geçen ilk 500 kelimeyi al
vectors = [word_vectors[word] for word in words]

# KMeans kümeleme: kelime vektörlerini kümelere ayır
kmeans = KMeans(n_clusters=2, random_state=42)  # n_clusters: kaç küme olacağı
kmeans.fit(vectors)
clusters = kmeans.labels_  # Her kelimenin ait olduğu küme

# PCA ile boyut indirgeme: 50 boyuttan 2 boyuta düşürülüyor
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(vectors)

# 2D görselleştirme
plt.figure(figsize=(12, 10))  # Grafik boyutu
plt.scatter(reduced_vectors[:, 0], reduced_vectors[:, 1], c=clusters, cmap="viridis")  # Küme renkleri

# Küme merkezlerini görselleştir
centers = pca.transform(kmeans.cluster_centers_)
plt.scatter(centers[:, 0], centers[:, 1], c="red", marker="x", s=120, label="Merkez")

plt.legend()

# Kelime etiketleri ekleniyor
for i, word in enumerate(words):
    plt.text(reduced_vectors[i, 0], reduced_vectors[i, 1], word, fontsize=8)

plt.title("Word2Vec - KMeans Kümeleme")
plt.xlabel("Bileşen 1")
plt.ylabel("Bileşen 2")
plt.grid(True)
plt.show()
