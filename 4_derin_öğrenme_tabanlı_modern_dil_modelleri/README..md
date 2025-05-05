# Derin Öğrenme Tabanlı Dil Modelleri

Bu klasör, doğal dil işleme (NLP) alanında yaygın olarak kullanılan derin öğrenme temelli dil modelleme tekniklerini içermektedir. RNN, LSTM gibi klasik sinir ağı yapılarının yanı sıra Transformer tabanlı modern büyük dil modelleri de yer almaktadır.

---

## Dosyalar ve Açıklamaları

- `1_RNN.ipynb`: Recurrent Neural Network (RNN) ile sıralı verilerdeki bağımlılıkları öğrenir.
- `2_LSTM.ipynb`: Long Short-Term Memory (LSTM) modeli ile uzun süreli bağlam bilgilerini koruyarak dil modelleme gerçekleştirir.
- `3_Bert_transformers.ipynb`: BERT modeli ile çift yönlü bağlam temelli dil temsil öğrenimi yapar.
- `4_gpt_transformers.ipynb`: GPT modeliyle tek yönlü bağlam kullanarak dil üretimi yapar.
- `5_LLAMA_transformers.ipynb`: LLaMA modelini kullanarak düşük kaynaklarla güçlü performans sağlar.

---

## Konsept Tanımları

### RNN (Recurrent Neural Network)
RNN, sıralı verilerdeki bağımlılıkları öğrenmeye yönelik bir yapıdır. Girdi dizileri sırayla işlenir ve her adımda bir gizli durum taşır. Bu gizli durum, bir önceki adımda elde edilen bilgiyi içerir ve sonraki adımlarda kullanılır. Ancak, RNN’ler uzun süreli bağımlılıkları öğrenme konusunda zorluk yaşayabilirler çünkü zamanla, daha eski bilgiler kaybolabilir. Bu sebeple, RNN’ler genellikle kısa bağımlılıkları modellemek için daha etkilidir.

### LSTM (Long Short-Term Memory)
LSTM, RNN yapısının geliştirilmiş bir versiyonudur. Geleneksel RNN’ler, uzun vadeli bağımlılıkları öğrenmede zorluk çekerken, LSTM'ler, hücre durumu ve kapı mekanizmaları kullanarak bu sorunu çözer. LSTM, geçmiş bilgileri "unutmama" yeteneğine sahip olup, uzun dönemli verilerin etkili bir şekilde öğrenilmesini sağlar. Bu özellik, özellikle metinlerin ya da zaman serisi verilerinin modellemesinde büyük avantaj sağlar.

### Transformers
Transformer, geleneksel sıralı hesaplamalardan farklı olarak paralel hesaplamaya olanak tanıyan bir modeldir. Bu model, metindeki her kelimeye dikkat (attention) mekanizması aracılığıyla farklı ağırlıklar atar, yani her kelimeyi diğer kelimelerle ilişkilendirerek bağlamı anlamaya çalışır. Bu özellik, klasik RNN ve LSTM'lere göre çok daha hızlı ve verimli bir şekilde bağlamsal ilişkileri öğrenmeyi sağlar. Transformers, günümüzde BERT, GPT gibi büyük dil modellerinin temelini oluşturur.

### BERT (Bidirectional Encoder Representations from Transformers)
BERT, bir transformer tabanlı dil modelidir ve metinleri çift yönlü olarak işler. Bu, hem önceki hem de sonraki kelimeler arasındaki bağlamı dikkate alarak dilin daha derin bir anlamını çıkarır. BERT, maskeli dil modelleme (Masked Language Modeling - MLM) tekniğiyle eğitilir; bu yöntemde, kelimeler rastgele maskelenir ve model, bu maskelenmiş kelimeleri tahmin etmeye çalışır. BERT, özellikle dil anlayışı görevlerinde (soru yanıtlama, metin sınıflandırma) son derece başarılıdır.

### GPT (Generative Pre-trained Transformer)
GPT, transformer tabanlı bir dil modelidir ve tek yönlü bir yapı kullanır. Bu model, metni sağdan sola doğru işler ve cümle üretimi gibi görevlerde oldukça başarılıdır. GPT, metin üretirken önceki kelimelere dayanarak sonraki kelimeleri tahmin eder. Genellikle cümle tamamlama, sohbet botları ve metin oluşturma gibi görevlerde kullanılır. GPT'nin güçlü yönü, büyük miktarda veriye dayanarak eğitim almış olması ve dil üretimindeki esnekliğidir.

### LLaMA (Large Language Model Meta AI)
LLaMA, Meta tarafından geliştirilen, açık kaynaklı ve yüksek verimliliğe sahip bir transformer tabanlı dil modelidir. LLaMA, modern büyük dil modelleri gibi çok sayıda parametreye sahip olsa da, kaynak kullanımı açısından oldukça verimlidir. Düşük kaynaklarla güçlü bir performans sunan bu model, büyük dil modelleri için daha erişilebilir bir seçenek olarak öne çıkar. LLaMA, büyük veri setlerinde eğitilmiş ve dil anlayışı ile üretimi konusunda oldukça yeteneklidir.

---
