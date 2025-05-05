import pandas as pd 

data = pd.read_csv("spam.csv", encoding = "latin-1")

data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis = 1, inplace = True)

data.columns = ["label", "text"]  # Veri çerçevesindeki sütun isimlerini "label" (etiket) ve "text" (mesaj) olarak değiştirir.

# Eksik değerlerin kontrolü (EDA)
data.isnull().sum()  # Eksik veri olup olmadığını kontrol eder, her sütundaki eksik değer sayısını gösterir.

import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

import re  # Düzenli ifadeler için re modülünü içeri aktarır.
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

text = list(data["text"])
lemmatizer = WordNetLemmatizer()

corpus = []  # İşlenmiş metinlerin saklanacağı listeyi başlatır.
for i in range(len(text)):  # Her bir mesaj üzerinde işlem yapılacak.
    r = re.sub("[^a-zA-Z]", "", text[i])  # Sadece İngilizce harfleri bırakır, sayılar ve noktalama işaretlerini temizler.
    r = r.lower()  # Metni küçük harfe dönüştürür.
    r = r.split()  # Metni kelimelere ayırır.
    r = [word for word in r if word not in stopwords.words("english")]  # Stopwords listesindeki kelimeleri çıkarır.
    r = [lemmatizer.lemmatize(word) for word in r]  # Her kelimeyi kök haline getirir (lemmatization).
    r = " ".join(r)  # Kelimeleri tekrar birleştirir ve metni oluşturur.
    corpus.append(r)  # İşlenmiş metni corpus listesine ekler.

data["text2"] = corpus  # "text2" adlı yeni sütun oluşturur ve işlenmiş metinleri buraya ekler.

x = data["text2"]  # Girdi verisi olarak "text2" sütununu seçer.
y = data["label"]  # Etiket verisi olarak "label" sütununu seçer.

# Eğitim ve test verilerini ayırma
from sklearn.model_selection import train_test_split  # Eğitim ve test verisini ayıran fonksiyonu içeri aktarır.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 42)  # Veriyi %67 eğitim, %33 test olarak böler.

# Özellik çıkarımı: Bag of Words (Kelime Çantası) modeli
from sklearn.feature_extraction.text import CountVectorizer  # Metin verisini sayısal veriye dönüştürmek için CountVectorizer'ı içeri aktarır.
cv = CountVectorizer()  # CountVectorizer nesnesini oluşturur.
x_train_cv = cv.fit_transform(x_train)  # Eğitim verisini sayısal hale getirir.

# Model eğitimi: Karar Ağacı (Decision Tree)
from sklearn.tree import DecisionTreeClassifier  # Karar Ağacı sınıflandırıcısını içeri aktarır.
dt = DecisionTreeClassifier()  # Karar Ağacı modelini oluşturur.
dt.fit(x_train_cv, y_train)  # Modeli eğitim verisiyle eğitir.

x_test_cv = cv.transform(x_test)  # Test verisini aynı özelliklere dönüştürür (eğitim verisinde kullanılan CountVectorizer ile).

# Tahmin yapma
predictions = dt.predict(x_test_cv)  # Test verisi üzerinde tahminler yapar.

from sklearn.metrics import confusion_matrix  # Karışıklık matrisini hesaplamak için gerekli fonksiyonu içeri aktarır.
c_matrix = confusion_matrix(y_test, predictions)  # Gerçek ve tahmin edilen etiketleri karşılaştırarak karmaşıklık matrisini oluşturur.

# Karışıklık matrisi
#     0    1
# 0  TN   FP
# 1  FN   TP
# TN: True Negative (Doğru Negatif), FP: False Positive (Yanlış Pozitif), FN: False Negative (Yanlış Negatif), TP: True Positive (Doğru Pozitif)

correct = c_matrix[0,0] + c_matrix[1,1]  # Doğru sınıflandırılan örneklerin sayısını hesaplar (TP + TN).
total = c_matrix.sum()  # Tüm örneklerin toplamını hesaplar (TP + TN + FP + FN).
print("Accuracy: ", 100 * (correct / total))  # Doğruluk oranını hesaplar ve ekrana yazdırır.
