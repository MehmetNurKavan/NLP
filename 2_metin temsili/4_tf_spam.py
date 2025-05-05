import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("spam.csv")

# tf-idf
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(df["text"])

# kelime kumesi
feature_names = vectorizer.get_featrue_names_out()
tfidf_score = x.mean(axis= 0).A1 # ortlamaa tf-idf degeri

df_tfidf = pd.DataFrame ({"word": feature_names, "tfidf_score": tfidf_score})

df_tfidf_sorted = df_tfidf.sort_values(by = "tfidf_score", ascending = False)

print(df_tfidf_sorted)
