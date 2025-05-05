# NLP Projesi

Bu proje, **Türkcell Geleceği Yazılımcılar** programında aldığım eğitim ile derlenen ve **Kaan Can Yılmaz** hocadan aldığım bilgilerle kodlanmış bir doğal dil işleme (NLP) projesidir. Proje, çeşitli NLP görevlerini gerçekleştirirken kullanılan farklı teknikleri ve modelleri içermektedir.

## İçerik

- [Regex ve Metin Temizleme](#regex-ve-metin-temizleme)
- [Olasılıksal ve Derin Öğrenme Tabanlı Modeller](#olasılıksal-ve-derin-öğrenme-tabanlı-modeller)
- [Temel NLP Görevleri](#temel-nlp-görevleri)
- [Gelişmiş NLP Görevleri](#gelişmiş-nlp-görevleri)

---

## Regex ve Metin Temizleme

Bu bölüm, **Python regex (re modülü)** ile düzenli ifadeler kullanarak metin temizleme ve analiz işlemlerini ele almaktadır. Metinlerin işlenmesinde sıklıkla kullanılan regex ile;

- Karakter sınıfları ve özel karakterler (`\d`, `\w`, `^`, vb.)
- Metin temizleme, stop word çıkarma, tokenizasyon gibi işlemler yapılır.

Ayrıca, **text_cleaning.py**, **tokenization.py** ve **stop_word.py** gibi dosyalar metinlerin ön işleme sürecinde kullanılan temel fonksiyonları içermektedir.

---

## Olasılıksal ve Derin Öğrenme Tabanlı Modeller

Bu klasör, farklı **olasılıksal dil modelleri** ve **derin öğrenme tabanlı transformer modelleri** içerir.

- **N-gram** ve **HMM (Hidden Markov Model)** ile kelime geçiş olasılıklarını modelleme.
- **LSTM (Long Short-Term Memory)** ve **RNN (Recurrent Neural Networks)** ile zaman serisi verisi analizi.
- **BERT**, **GPT** ve **LLaMA** gibi **transformer tabanlı modeller** ile dilin bağlamsal ilişkisini öğrenme.

Her bir modelin uygulanabilirlik alanları ve kullanım detayları **1_n_gram.ipynb**, **2_hmm.ipynb** gibi dosyalarda yer almaktadır.

---

## Temel NLP Görevleri

Aşağıdaki temel NLP görevlerine dair örnekler bulunmaktadır:

- **Metin Sınıflandırma**: Metinleri önceden tanımlanmış kategorilere ayırma.
- **Duygu Analizi**: Kullanıcı yorumlarından duygu tespiti yapma.
- **POS Etiketleme**: Metindeki kelimelere gramatikal etiketler atama.
- **Adlandırılmış Varlık Tanıma (NER)**: Kişi, yer, tarih gibi önemli varlıkları tanıma.

Bu görevler için temel modeller **POS etiketi çıkarma**, **sentiment analysis** gibi uygulamalarla ilgili ayrıntılar mevcuttur.

---

## Gelişmiş NLP Görevleri

- **Makine Çevirisi**: Farklı diller arasında metin çevirisi yapma.
- **Soru-Cevap Sistemleri**: Metinlerden veya veritabanlarından kullanıcıya anlamlı cevaplar sağlama.
- **Metin Özetleme**: Uzun metinlerin daha kısa ve öz hale getirilmesi.
- **Dialog Sistemleri**: İnsanla etkileşimli, doğal dilde sohbet sistemleri geliştirme.

Bu görevler için derin öğrenme ve transformer tabanlı teknikler daha güçlü sonuçlar sunar.

---

## Uygulama

Projede kullanılan tüm yöntemler ve modeller, gerçek dünyada pek çok farklı uygulama alanına yönlendirilebilir. Örneğin:

- **Chatbot geliştirme**: Kullanıcılarla doğal dilde etkileşim kuran sistemler.

---
