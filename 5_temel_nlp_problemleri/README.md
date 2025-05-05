# NLP Uygulama Örnekleri

Bu proje, doğal dil işleme (NLP) alanında yaygın olarak kullanılan çeşitli uygulamaları tanıtan örnekler içermektedir. Metin sınıflandırma, adlandırılmış varlık tanıma (NER), morfolojik çözümleme, sözcük türü etiketleme (POS), sözcük anlamı ayrımı (WSD) ve duygu analizi gibi temel NLP görevlerine odaklanılmaktadır.

## Dosyalar ve Açıklamaları

- `0_versiyon_library.ipynb`: Projeye ait kütüphanelerin ve bağımlılıkların yüklendiği ve versiyonlarının kontrol edildiği Jupyter Notebook dosyası.
- `1_text_classification.py`: Metin sınıflandırma modelinin eğitim ve test işlemleri gerçekleştirilir. Veri ön işleme, model oluşturma ve doğrulama adımlarını içerir.
- `2_named_entity_recognition.py`: Adlandırılmış varlık tanıma (NER) işlemini gerçekleştirir. Metin içerisindeki kişi, yer, organizasyon gibi varlıkları tanır.
- `3_morphological_analysis.py`: Kelimelerin morfolojik çözümlemesini yapar. Kelimeleri köklerine ve eklerine ayırarak dil bilgisel özellikleri analiz eder.
- `4_part_of_speech_tagging.py`: Cümledeki kelimelere dil bilgisel etiketler (isim, fiil, sıfat vb.) atar. Kelimelerin hangi türde olduğunu belirler.
- `5_word_sense_disambiguation.py`: Çok anlamlı kelimelerin bağlam içerisindeki doğru anlamını belirler. Kelimenin doğru anlamını ayrıştırmak için bağlam analiz edilir.
- `6_sentiment_analysis.py`: Duygu analizi gerçekleştirir. Metnin olumlu, olumsuz veya nötr bir duygu içerip içermediğini tespit eder.
- `7_dugu_analizi.py`: Türkçe metinlerde duygu analizi yapar. Metnin genel duygu eğilimini (olumlu, olumsuz, nötr) belirler ve sonuçları sunar.

## 📁 Veri Setleri

- `IMDB Dataset.csv` : IMDB film yorumlarını içerir.
- `Spam.csv` : Spam ve ham e-postaları içerir.

---

## Modüller ve Açıklamaları

### 1. **Text Classification – Metin Sınıflandırma**
Metin verilerinin içeriklerine göre belirli kategorilere ayrılmasıdır.

**Kullanım Alanları:**

| Alan                        | Açıklama                                                              |
|-----------------------------|-----------------------------------------------------------------------|
| Duygu Analizi               | Yorumların olumlu, olumsuz veya nötr olup olmadığını belirler.        |
| Haber Sınıflandırma         | Haberleri kategorilere (spor, siyaset vb.) ayırır.                   |
| Spam Tespiti                | E-postaları spam / spam değil olarak etiketler.                      |
| Konu Tespiti                | Metnin hangi konuyla ilgili olduğunu belirler.                       |
| Destek Talebi Sınıflandırma| Teknik destek taleplerini ilgili kategoriye yönlendirir.             |

---

### 2. **Named Entity Recognition (NER) – Adlandırılmış Varlık Tanıma**
Metin içinde özel isimleri, yerleri, organizasyonları ve sayısal ifadeleri tanır.

📌 **Kullanım Alanları:**

| Alan                         | Açıklama                                                           |
|------------------------------|--------------------------------------------------------------------|
| Kişi İsimleri                | Ahmet, John, Elon Musk gibi kişi adlarını tanımlar.                |
| Yer İsimleri                 | İstanbul, Paris, New York gibi konumları tespit eder.              |
| Organizasyonlar              | Microsoft, OpenAI, TÜBİTAK gibi varlıkları etiketler.              |
| Tarih / Zaman                | “15 Nisan 2023”, “sabah 9” gibi ifadeleri tanımlar.                |
| Para, Yüzde, Ölçü Birimleri | “50 TL”, “%15”, “3 kilometre” gibi ölçüleri tanımlar.              |

---

### 3. **Morphological Analysis – Morfolojik Çözümleme**
Kelimeleri kök ve eklerine ayırarak gramatik özelliklerini belirler.

📌 **Kullanım Alanları:**

| Alan                          | Açıklama                                                           |
|-------------------------------|--------------------------------------------------------------------|
| Kök Bulma                    | Örneğin: "geldim" → kök: **gel**                                   |
| Ek Ayırımı                   | “gel-di-m” → kök: **gel**, zaman: **-di**, şahıs: **-m**           |
| Gramer Özellikleri Çıkarımı | Zaman, şahıs, çoğulluk gibi bilgileri elde eder.                  |
| NLP Model Girdileri         | Anlamlandırma, çeviri, özetleme gibi görevlerde temel bilgidir.    |

---

### 4. **Part of Speech (POS) – Sözcük Türü Etiketleme**
Cümledeki kelimelerin dilbilgisel türlerini belirler: isim, fiil, zarf vb.

**Kullanım Alanları:**

| Alan                    | Açıklama                                                              |
|-------------------------|-----------------------------------------------------------------------|
| Cümle Yapısını Anlama  | Kelimelerin cümledeki görevlerini analiz eder.                         |
| Dil Modeli Eğitimi     | Girdiler için dilbilgisel bağlam sağlar.                              |
| Makine Çevirisi        | Her kelimenin doğru anlamda çevrilmesini sağlar.                      |
| Yazım Denetimi / Özetleme | Hatalı kullanım tespiti ve bilgi odaklı özetleme sağlar.             |

---

### 5. 🔍 **Word Sense Disambiguation (WSD) – Sözcük Anlamı Ayrımı**
Çok anlamlı kelimelerin bağlam içinde doğru anlamını belirleme işlemidir.

**Kullanım Alanları:**

| Alan                          | Açıklama                                                             |
|-------------------------------|----------------------------------------------------------------------|
| Anlam Ayrımı                  | Örneğin “bank” kelimesinin “banka” mı “nehir kıyısı” mı olduğunu belirleme. |
| Bağlam Tabanlı Anlam Çıkarımı | Kelimenin kullanıldığı bağlama göre anlam çözümlemesi yapılır.       |
| NLP Uygulamaları              | Çeviri, metin özetleme ve anlam analizinde doğru yorum sağlar.       |

---

### 6. 😊 **Sentiment Analysis – Duygu Analizi**
Metnin olumlu, olumsuz veya nötr bir duygu içerip içermediğini belirler.

**Kullanım Alanları:**

| Alan                          | Açıklama                                                            |
|-------------------------------|---------------------------------------------------------------------|
| Sosyal Medya İzleme          | Kullanıcı yorumlarını analiz ederek genel duygu eğilimini tespit eder. |
| Müşteri Geri Bildirimleri    | Ürün/servis hakkında yapılan yorumların duygu analizini sunar.     |
| Pazar Araştırması            | Tüketici hissiyatını anlamaya yönelik analiz sağlar.               |
| Yorum Analizi                | Film, kitap, ürün yorumlarını kategorilere ayırır.                 |

---
