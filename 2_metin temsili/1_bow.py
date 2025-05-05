# Metin Temsili (Text Representation)
# Metin Temsili, bir metini sayısal veya başka bir formatta temsil etme işlemidir.

from sklearn.feature_extraction.text import CountVectorizer

documents = {
    "Kedi evde",
    "Kedi bahçede"
    }

vectorizer = CountVectorizer()

# metin -> sayisal vektor
x= vectorizer.fit_transform(documents)

# kelime kumesi {"kedi", "evde","bahçede"}
print("Kelime Kümesi: ", vectorizer.get_feature_names_out())


# vector temsili
print("Vektor temsili:", x.toarray())

'''
Kelime Kümesi:  ['bahçede' 'evde' 'kedi']
Vektor temsili: 
    [[1 0 1]
    [0 1 1]]
'''