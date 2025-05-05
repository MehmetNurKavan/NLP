# odev
# than themn out zamerli edat baglacları çıakrtı
# number of clas 2-3 olabilir
# pca 3 yapip 3 boyutlu gorsellestir
# diger dosyada var cozumu

# kutuphanelerin iceriye aktarilamsi
import pandas as pd
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import re
from mpl_toolkits.mplot3d import Axes3D  # 3D görselleştirme için

# veri setinin yuklenmesi
df = pd.read_csv("IMDB Dataset.csv")
print(df.head(10))
documents = df["review"]

# çıkarılacak zamir ve edatlar listesi
stopwords = ["than", "them", "out", "the", "and", "for", "but", "or", "yet", "so", 
             "in", "on", "at", "by", "with", "about", "against", "between",
             "into", "through", "during", "before", "after", "above", "below",
             "to", "from", "up", "down", "off", "over", "under", "again", "further",
             "then", "once", "here", "there", "when", "where", "why", "how",
             "all", "any", "both", "each", "few", "more", "most", "other", "some", "such",
             "no", "nor", "not", "only", "own", "same", "that", "this", "too", "very"]

# metin temizleme
def clean_text(text):
    text = text.lower()  # kucuk harf
    text = re.sub(r"\d+", "", text)  # sayilari temizle
    text = re.sub(r"[^\w\s]", "", text)  # ozel karakterleri temizleme
    
    # zamir ve edatları çıkartma & kısa kelimeleri temizleme
    text = " ".join([word for word in text.split() if len(word) > 2 and word not in stopwords])
    return text

cleaned_documents = [clean_text(doc) for doc in documents] 

# cumeleri tokenizasyon islemi
tokenized_documents = [simple_preprocess(doc) for doc in cleaned_documents]

# word2vec modeli tanimlayalim
model = Word2Vec(sentences=tokenized_documents, vector_size=50, window=5, min_count=3, sg=1)
word_vectors = model.wv

words = list(word_vectors.index_to_key)[:500]
vectors = [word_vectors[word] for word in words]

# clustering 3 adet kume olusturma
n_clusters = 3  # 2 veya 3 küme kullanabilirsiniz
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(vectors)
clusters = kmeans.labels_

# pca 50boyut -> 3boyut donsuumu
pca = PCA(n_components=3)
reduced_vectors = pca.fit_transform(vectors)

# 3D gorsellestirme
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot oluşturma
scatter = ax.scatter(
    reduced_vectors[:, 0],
    reduced_vectors[:, 1],
    reduced_vectors[:, 2],
    c=clusters,
    cmap="viridis",
    alpha=0.7
)

# Küme merkezlerini gösterme
centers = pca.transform(kmeans.cluster_centers_)
ax.scatter(
    centers[:, 0],
    centers[:, 1],
    centers[:, 2],
    c="red",
    marker="x",
    s=200,
    label="Merkezler"
)

# Eksenleri etiketleme
ax.set_xlabel('Bileşen 1')
ax.set_ylabel('Bileşen 2')
ax.set_zlabel('Bileşen 3')

# En popüler kelimeleri çizim üzerine ekleyelim (tüm kelimeler çok kalabalık olur)
# Her kümeden belirli sayıda kelime gösterelim
words_per_cluster = 20
for cluster_id in range(n_clusters):
    # Bu kümeye ait kelimelerin indekslerini bulalım
    cluster_indices = [i for i, label in enumerate(clusters) if label == cluster_id]
    
    # Her kümeden en fazla words_per_cluster kadar kelime gösterelim
    for idx in cluster_indices[:words_per_cluster]:
        ax.text(
            reduced_vectors[idx, 0],
            reduced_vectors[idx, 1],
            reduced_vectors[idx, 2],
            words[idx],
            fontsize=8
        )

plt.title(f"Word2Vec - {n_clusters} Küme ile 3D PCA Görselleştirmesi")
plt.legend()
plt.tight_layout()
plt.show()

# Kümeleri analiz edelim
print(f"\n{n_clusters} Küme Analizi:")
for cluster_id in range(n_clusters):
    cluster_words = [words[i] for i, label in enumerate(clusters) if label == cluster_id]
    print(f"Küme {cluster_id}: {', '.join(cluster_words[:20])}...")
