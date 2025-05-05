import pandas as pd
from gensim.models import Word2Vec, FastText
from gensim.utils import simple_preprocess
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Örnek cümleler – Türkçe dilinde hayvan temalı cümleler
sentences = [
    "Kedi çok tatlı bir hayvandır.",
    "Köpekler evcil hayvanlardır.",
    "Kediler genellikle mutludur.",
    "Köpekler sadık ve dost canlısıdır.",
    "Hayvanlar insanlar için iyi arkadaşlardır.",
]

# Cümleleri kelime listelerine dönüştürüyoruz (ön işlem: küçük harfe çevirme, noktalama temizleme vs.)
tokenized_sentences = [simple_preprocess(sentence) for sentence in sentences]

# Word2Vec modeli (CBOW)
# vector_size: her kelimenin kaç boyutlu vektörle temsil edileceği
# window: bir kelimenin çevresinde kaç kelimeye bakılacağı
# min_count: modelin en az kaç defa geçen kelimeleri dikkate alacağı
# sg: 0 = CBOW (Context to Word), 1 = Skip-gram
word2vec_model = Word2Vec(tokenized_sentences, vector_size=50, window=5, min_count=1, sg=0)

# FastText modeli
# FastText, bilinmeyen kelimeleri de alt-kelimelere (subword) ayırarak öğrenebilir.
fasttext_model = FastText(tokenized_sentences, vector_size=50, window=5, min_count=1, sg=0)

# Kelime gömme (embedding) vektörlerini görselleştirme fonksiyonu
def plot_word_embeddings(model, title):
    word_vectors = model.wv  # Kelime vektörlerini al
    words = list(word_vectors.index_to_key)[:100]  # İlk 100 kelimeyi al
    vectors = [word_vectors[word] for word in words]  # Her kelimenin vektörünü al

    # PCA ile boyut indirgeme (50 boyuttan 3 boyuta)
    pca = PCA(n_components=3)
    reduced_vectors = pca.fit_transform(vectors)

    # 3D görselleştirme için grafik oluştur
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection="3d")

    # 3D noktaları çiz
    ax.scatter(reduced_vectors[:, 0], reduced_vectors[:, 1], reduced_vectors[:, 2])

    # Her kelimeyi görselleştirme üzerinde yaz
    for i, word in enumerate(words):
        ax.text(reduced_vectors[i, 0], reduced_vectors[i, 1], reduced_vectors[i, 2], word, fontsize=12)

    ax.set_title(title)
    ax.set_xlabel("Component 1")
    ax.set_ylabel("Component 2")
    ax.set_zlabel("Component 3")
    plt.show()

# Görselleştirmeyi çağır
plot_word_embeddings(word2vec_model, "Word2Vec ile Kelime Gösterimi")
plot_word_embeddings(fasttext_model, "FastText ile Kelime Gösterimi")
