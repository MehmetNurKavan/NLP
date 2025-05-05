# Named Entity Recognition (NER)

import pandas as pd
import spacy

try:
    # Modeli yükle
    nlp = spacy.load("en_core_web_sm")
    print("Model başarıyla yüklendi!")
except Exception as e:
    print(f"Hata: {e}")

content = "John used to work at Microsoft but now lives alone in New York. He once visited the National History Museum, reminiscing about better days."

# Metni NLP modeline gönderiyoruz
doc = nlp(content)

# Varlıkları yazdır (ent: entity → varlık)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

# Varlıkları listeye kaydet (label ve lemma da dahil)
entities = [(ent.text, ent.label_, ent.lemma_) for ent in doc.ents]

# DataFrame oluştur
df = pd.DataFrame(entities, columns=["Text", "Label", "Lemma"])
