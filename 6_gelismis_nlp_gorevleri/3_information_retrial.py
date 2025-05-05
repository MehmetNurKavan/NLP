from transformers import BertTokenizer, BertModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Kullanılacak BERT modelinin adı
model_name = "bert-base-uncased"

# Tokenizer ve model BERT'in önceden eğitilmiş sürümünden yükleniyor
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# Analiz edilecek belgeler (cümleler)
'''
bu ornekte biribirne cok yakınlar degerler ve farklı bir sonuc veriyor
documents = [
    "Machine Learning is a branch of artificial intelligence that allows computers to learn from data and make decisions without being explicitly programmed.",
    "Natural Language Processing is a field of AI that focuses on enabling machines to understand, interpret, and generate human language.",
    "Artificial Intelligence refers to the simulation of human intelligence in machines that are designed to think, learn, and solve problems like humans.",
    "Data Science is the process of analyzing large amounts of data to extract meaningful insights using techniques from statistics, machine learning, and computer science.",
    "Deep Learning is a subset of machine learning that uses neural networks with many layers to model complex patterns in data.",
    "Neural Networks are computational models inspired by the human brain, consisting of layers of interconnected nodes that can learn to perform tasks by considering examples.",
]
'''

# bu ornekte biraz daha uzak ornekelr var
documents = [
    "Machine Learning is a branch of artificial intelligence that allows computers to learn from data and make decisions without being explicitly programmed.",
    "The Eiffel Tower is one of the most iconic structures in the world, located in Paris, France.",
    "Natural Language Processing is a field of AI that focuses on enabling machines to understand, interpret, and generate human language.",
    "My old computer finally stopped working after years of faithful service.",
    "The dog barked excitedly as its owner returned home from work.",
    "The sun sets beautifully over the mountains, painting the sky in shades of orange and pink.",
]



# Kullanıcının sorduğu doğal dil sorgusu
query = "What is machine learning?"

# Bu fonksiyon bir metni (document ya da query) BERT gömme (embedding) vektörüne dönüştürür
def get_embedding(text):
    # Metni tokenize et ve giriş tensörlerine dönüştür (padding ve truncation ile)
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    # Modelden çıktıyı al
    outputs = model(**inputs)

    # Tüm token'ların son katman çıktısı (batch_size, seq_len, hidden_size)
    last_hidden_state = outputs.last_hidden_state

    # Ortalama alma yöntemiyle tüm token'ların vektörlerinin ortalaması alınır
    embedding = last_hidden_state.mean(dim=1)

    # PyTorch tensörünü NumPy dizisine dönüştür
    return embedding.detach().numpy()

# Belgeler için gömme (embedding) vektörleri elde edilir
doc_embeddings = np.vstack([get_embedding(doc) for doc in documents])

# Sorgu için embedding vektörü
query_embedding = get_embedding(query)

# Sorgu ile belgeler arasındaki cosine similarity hesaplanır (benzerlikler)
similarities = cosine_similarity(query_embedding, doc_embeddings)

for i, score in enumerate(similarities[0]):
    print(f"Document {i+1} Similarity Score: {score:.4f}")

most_similar_idx = np.argmax(similarities)
print("\nMost relevant document:")
print(documents[most_similar_idx])
print(f"Score: {similarities[0][most_similar_idx]:.4f}")