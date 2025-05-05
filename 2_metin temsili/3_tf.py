from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

documents = [
    "Kedi çok tatlı bir hayvandır.",
    "Kedi ve köpekler çok tatlı hayvanlardır.",
    "Arılar bal üretirler."
    ]

tfidf_vectorizer = TfidfVectorizer()

# metin sayisallstirma, metin -> sayisal
x = tfidf_vectorizer.fit_transform(documents)

# kelime kumesi
feature_names = tfidf_vectorizer.get_feature_names_out()

print("TF-IDF Vektor temsilleri:")
vector_temsili = x.toarray()
print(vector_temsili)

df_tfidf =pd.DataFrame(vector_temsili, columns = feature_names)

kedi_tfidf = df_tfidf["kedi"]
kedi_mean_tfdf = np.mean(kedi_tfidf)


'''
TF-IDF Vektor temsilleri:
[[0.         0.         0.51741994 0.51741994 0.         0.3935112
  0.         0.3935112  0.         0.3935112  0.        ]
 [0.         0.         0.         0.         0.45954803 0.34949812
  0.45954803 0.34949812 0.45954803 0.34949812 0.        ]
 [0.57735027 0.57735027 0.         0.         0.         0.
  0.         0.         0.         0.         0.57735027]]
'''