from transformers import AutoTokenizer, AutoModel
import torch

# model ve tokenizer yukelme
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# metin tanimla
text = "Transformers are amazing for natural language processing."

# metin tokenlara donusumu
inputs = tokenizer(text, return_tensors="pt")

# modeli kullanrak metin temsili olsutur
with torch.no_grad(): # modelin agırlikalri guncellenilmeicek
    outputs = model(**inputs)

# cikislardan ilk tokenlari alalim
last_hidden_state = outputs.last_hidden_state
first_token_embedding = last_hidden_state[0, 0, :].cpu().numpy()

print("Metin temsili: ilk token: ")
print(first_token_embedding)