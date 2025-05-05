# Metin Temsili Yöntemleri

Bu klasör, doğal dil işleme (NLP) projelerinde metinlerin sayısal temsillere dönüştürülmesi için kullanılan farklı yöntemleri içermektedir.

## Dosyalar ve Açıklamaları

- `1_bow.py`: Bag of Words yöntemiyle temel metin temsili
- `2_bow_imdb.py`: IMDB yorumları üzerinde BoW uygulaması
- `3_tf.py`: Term Frequency (TF) hesaplama
- `4_tf_spam.py`: Spam tespiti için TF tabanlı temsil
- `5_ngram.py`: N-gram (bigram/trigram) ile geliştirilmiş BoW
- `6_word_embedded.py`: Word2Vec / GloVe ile kelime gömme temsili
- `7_word_embedded_IMDB.py`: IMDB veri setinde embedding + duygu analizi
- `8_wordembedding_odev.py`: Ödev amaçlı kelime gömme uygulaması
- `9_transformers.py`: BERT tabanlı transformer temsili

## 📁 Veri Setleri

- `IMDB Dataset.csv` : IMDB film yorumlarını içerir.
- `Spam.csv` : Spam ve ham e-postaları içerir.

---

## Yöntem Tanımları

### Bag of Words (BoW)
Her metni, içindeki kelimelerin sıklığına göre temsil eden basit ve etkili bir yöntemdir. Kelimelerin sırası ve bağlamı dikkate alınmaz.

### Term Frequency (TF)
Her kelimenin belgede kaç kez geçtiğini ölçer. BoW ile benzer olup, sadece sıklık değerine odaklanır.

### N-Gram
Kelimeleri tek tek değil, ikili (bigram), üçlü (trigram) gibi gruplar halinde analiz ederek bağlamsal ilişkilere daha duyarlı temsil sunar.

### Word Embedding
Kelimeleri anlamlarına göre çok boyutlu vektörlerde temsil eder. Benzer anlamdaki kelimeler vektör uzayında birbirine yakın olur.

### Transformers
Attention (dikkat) mekanizması kullanan derin öğrenme mimarisidir. Kelimeler arasındaki bağlamsal ilişkileri güçlü bir şekilde öğrenerek, metinlerin bağlama duyarlı temsillerini üretir. BERT, GPT gibi modern modeller bu mimari üzerine kuruludur.

---
