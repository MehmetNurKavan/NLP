# Metin Ön İşleme

Bu proje, doğal dil işleme (NLP) alanında metin ön işleme adımlarını gerçekleştiren çeşitli Python dosyalarından oluşmaktadır.

## Dosyalar ve Açıklamaları

- `text_cleaning.py`: Metin temizleme işlemleri (gereksiz semboller, rakamlar, özel karakterler vb.)
- `tokenization.py`: Tokenizasyon işlemleri (kelimeler veya cümleler ile metni parçalara ayırma)
- `stemming_lemmatization.py`: Stemming ve lemmatization işlemleri (kelimeleri köklerine indirgeme)
- `stop_word.py`: Durak kelimelerin (stop words) metinden çıkarılması

---

## Yöntem Tanımları

### Text Cleaning
Metin temizleme, ham metin verilerini anlamlı hale getirmek için yapılan bir işlemdir. Bu işlemde gereksiz semboller, rakamlar, özel karakterler ve durak kelimeler gibi öğeler temizlenir.

### Tokenization
Tokenizasyon, metni daha küçük parçalara (kelimeler veya cümleler gibi) ayırma işlemidir. Bu sayede metin, NLP işlemleri için uygun hale gelir.

### Stemming & Lemmatization
- **Stemming**: Kelimeleri köklerine indirgeme işlemidir. Kelimelerin türemiş halleri, köklerine dönüştürülür.
- **Lemmatization**: Kelimeleri, dil bilgisel olarak doğru hale getirerek köklerine indirgeme işlemidir.

### Stop Word Removal
Stop words (durak kelimeler), anlam taşımayan veya çok sık kullanılan kelimelerdir. Bu kelimeler, metinden çıkarılarak daha anlamlı bir metin elde edilir.

---
