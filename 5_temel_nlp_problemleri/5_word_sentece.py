import nltk
from nltk.wsd import lesk

nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("punkt")

sentence1 = "I went to the bank to deposit money"
word1 = "bank"
sense1 = lesk(nltk.word_tokenize(sentence1), word1)
# burda bank hem banka hem oturulacak yer hangisis diye bilmesi grek model

print("Sentence: ", sentence1)
print("Word: ", word1)
print("Sense: ", sense1.definiition())

'''
Sentence: The eiver bank wasflooded after the heavy rain.
word: bank
sense: a container(usually with a slot ain the top) for keeping money at home
'''
