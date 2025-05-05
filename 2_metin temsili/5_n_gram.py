from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "Bu bir örnek metindir",
    "Bu örnek metin doğal dil işlemeyi gösterir",
    ] 

vectorizer_unigram = CountVectorizer(ngram_range=(1,1))
vectorizer_bigram = CountVectorizer(ngram_range=(2,2))
vectorizer_trigram = CountVectorizer(ngram_range=(3,3))

x_unigram = vectorizer_unigram.fit_transform(documents)
unigram_features = vectorizer_unigram.get_feature_names_out()

x_bigram = vectorizer_bigram.fit_transform(documents)
bigram_features = vectorizer_bigram.get_feature_names_out()

x_trigram = vectorizer_trigram.fit_transform(documents)
trigram_features = vectorizer_trigram.get_feature_names_out()

print("unigram features ", unigram_features)
print("bigram features", bigram_features)
print("trigram_feature", trigram_features)
