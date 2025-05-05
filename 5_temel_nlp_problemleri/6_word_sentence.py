from pywsd.lesk import simple_lesk, adapted_lesk, cosine_lesk

sentences = [
    "I went to the bank to deposit money.",
    "The river bank was flooded after the heavy rain",
]
word = "bank"

for sentence in sentences:
    print("Sentence: ", sentence)
    sense_simple = simple_lesk(sentence, word)
    print("Sense simple: ", sense_adapted.definition())
    
    sense_adapted = adapted_lesk(sentence, word)
    print("Sense adapted: ", sense_adapted, word)
    
    sense_cosine = cosine_lesk(sentence, word)
    print("Sense cosine: ", sense_cosine.definition())
    