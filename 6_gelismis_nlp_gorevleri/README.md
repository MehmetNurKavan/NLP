# Gelişmiş NLP Görevleri

Bu klasör, çeşitli gelişmiş doğal dil işleme (NLP) görevlerini içeren Python dosyalarını içermektedir. Her bir dosya, farklı NLP teknikleri ve modelleri kullanarak belirli bir dil işleme görevini çözmeyi amaçlar.

---

## Dosyalar ve Açıklamaları

- `1_question_answer_bert.py`: BERT modeli kullanarak soru-cevap uygulaması. Model: `bert-large-uncased-whole-word-masking-finetuned-squad`.
- `2_question_answer_cpy.py`: GPT-2 modelini kullanarak soru-cevap uygulaması.
- `3_information_retrial.py`: Bilgi geri çağırma uygulaması. Model: `bert-base-uncased`.
- `4_recommendation_system_NN.py`: Sinir ağı kullanarak öneri sistemi. Küçük bir veri seti ile geliştirilmiştir.
- `5_recommendation_system_KNN.py`: KNN algoritması ile öneri sistemi. Veri seti: `MovieLens 100k`.
- `6_machine_translation.py`: Makine çevirisi uygulaması. Model: `Helsinki-NLP/opus-mt-en-fr` (İngilizce'den Fransızca'ya).
- `7_text_summarization.py`: Metin özetleme uygulaması. Kullanılan yöntem: `pipeline("summarization")`.
- `odev.txt`: Projeye dair notlar ve açıklamalar.

---

## Konsept Tanımları

### BERT (Bidirectional Encoder Representations from Transformers)
BERT, her iki yönden (soldan sağa ve sağdan sola) bağlamı öğrenen bir dil modelidir. Soru-cevap uygulamaları gibi görevlerde başarıyla kullanılır.

### GPT-2 (Generative Pre-trained Transformer 2)
GPT-2, metin üretme ve dil modelleme görevlerinde kullanılan güçlü bir dil modelidir. Soru-cevap gibi doğal dil anlama görevleri için de uygundur.

### LLAMA (Large Language Model Meta AI)
LLAMA, Meta tarafından geliştirilen büyük bir dil modelidir. Çeşitli NLP görevlerinde yüksek doğrulukla çalışır ve çok dilli uygulamalarda etkili sonuçlar verir. Metin üretimi, özetleme, soru-cevap gibi görevlerde kullanılır.

### KNN (K-Nearest Neighbors)
KNN, makine öğrenmesi algoritmalarından biridir ve veri noktalarını etiketlemek için kullanılır. Özellikle öneri sistemlerinde sıkça kullanılır.

### Sinir Ağı (Neural Network)
Sinir ağları, veri öğrenme ve tahminlerde bulunma kapasitesine sahip makine öğrenmesi algoritmalarıdır. Özellikle öneri sistemlerinde etkili olabilir.

### Makine Çevirisi
Makine çevirisi, bir dildeki metni başka bir dile çevirmeyi amaçlayan doğal dil işleme görevidir. `Helsinki-NLP/opus-mt-en-fr` modeli, İngilizce'den Fransızca'ya çeviri yapmaktadır.

### Metin Özetleme
Metin özetleme, uzun metinlerin kısa versiyonlarına indirgenmesidir. Bu görevde, metnin temel noktalarını koruyarak daha kısa bir metin üretilir.

---
