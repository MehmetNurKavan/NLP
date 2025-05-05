import pandas as pd 
import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords  # İngilizce stopwords (bağlaç, edat gibi anlam taşımayan kelimeler)
from nltk.tokenize import word_tokenize  # Metni kelimelere ayırma (tokenization)
from nltk.stem import WordNetLemmatizer  # Lemmatizasyon (kök formuna dönüştürme)

# NLTK'nin bazı lexicon dosyalarını indiriyoruz, bu dosyalar NLP işlemlerinde kullanılır
nltk.download("vader_lexicon")  # Sentiment analiz için lexicon
nltk.download("stopwords")  # Stopwords listesi
nltk.download("punkt")  # Kelime ayırıcılar için tokenizer
nltk.download("wordnet")  # Lemmatizer için WordNet veritabanı
nltk.download("omw-1.4")  # WordNet'in ek kaynakları

df = pd.read_csv("amazon.csv")

# Metni işleme fonksiyonu
def preproceess_text(text):
    # Metni küçük harfe çeviriyoruz ve kelimelere ayırıyoruz (tokenization)
    tokens = word_tokenize(text.lower())

    # Stopwords listesine göre gereksiz kelimeleri filtreliyoruz
    filtred_tokens = [token for token in tokens if token not in stopwords.words("english")]

    # Kelimeleri köklerine indiriyoruz (lemmatization)
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtred_tokens]

    # Kelimeleri tekrar birleştirerek işlenmiş metni elde ediyoruz
    processed_text = " ".join(lemmatized_tokens)

    # İşlenmiş metni döndürüyoruz
    return processed_text

# DataFrame'deki 'reviewText' sütunundaki metni işlemeye alıyoruz
df["reviewText2"] = df["reviewText"].apply(preproceess_text)

# Sentiment analizi için SentimentIntensityAnalyzer'ı başlatıyoruz
analyzer = SentimentIntensityAnalyzer()

# Sentiment analizini yapacak fonksiyonu tanımlıyoruz
def get_sentiment(text):
    # Metni analiz ederek duygu skorlarını alıyoruz
    scores = analyzer.polarity_scores(text)

    # Skorlara göre sentiment değeri belirliyoruz: Pozitif mi negatif mi?
    # Eğer pozitifse 1, değilse (negatif veya nötr) 0 döndürüyoruz
    sentiment = 1 if scores["pos"] > 0 else 0

    # Sentiment değerini döndürüyoruz
    return sentiment

# 'reviewText2' sütunundaki her bir metni sentiment analizine tabi tutuyoruz
df["sentiment"] = df["reviewText2"].apply(get_sentiment)

# Skorları ve başarıyı değerlendirmek için confusion matrix ve classification report yazdırıyoruz
from sklearn.metrics import confusion_matrix, classification_report

# Confusion matrix'i yazdırıyoruz (gerçek vs tahmin edilen)
print(confusion_matrix(df["Positive", df["sentiment"]]))
