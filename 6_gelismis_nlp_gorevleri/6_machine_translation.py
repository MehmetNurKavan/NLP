#%% Import libraries

from transformers import MarianMTModel, MarianTokenizer

#%% Initialize model and tokenizer

model_name = "Helsinki-NLP/opus-mt-en-fr"  # İngilizce'den Fransızca'ya çeviri yapacak model
tokenizer = MarianTokenizer.from_pretrained(model_name) # Tokenizer'ı model için başlat
model = MarianMTModel.from_pretrained(model_name)  # Modeli yükle

#%% Example text to translate

text = "Hello, what is your name?"

#%% Encode the text, provide it to the model as input

# Metni tokenize et ve modelin anlayacağı formatta hazırlamak için input tensor'larına dönüştür
translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))  # Modeli çalıştır, çeviriyi yap

#%% Decode the translation, convert it back to string

# Modelin çıktısını, token'ları geri metne çevir
translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)  # Çeviriyi çöz ve özel token'ları at

#%% Print the translated text

print(f"Translated text: {translated_text}")
