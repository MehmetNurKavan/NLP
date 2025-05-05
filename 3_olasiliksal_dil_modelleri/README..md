# Olasılıksal Dil Modelleri

Bu klasör, olasılıksal yaklaşımlarla geliştirilen dil modelleme tekniklerini içermektedir. Her bir dosya, metinlerin istatistiksel özelliklerinden faydalanarak doğal dil işleme görevlerini çözmeyi amaçlar.

---

## Dosyalar ve Açıklamaları

- `1_n_gram.ipynb`: N-gram modeli ile kelimeler arasındaki geçiş olasılıklarını hesaplar. Unigram, bigram ve trigram gibi farklı yapıların örnekleri içerir.
- `2_hmm.ipynb`: Gizli Markov Modeli (HMM) ile etiketlenmemiş kelime dizilerinin ardında yatan gizli durumları tahmin eder. POS etiketleme gibi görevlerde kullanılır.
- `3_hmm_conll2000.ipynb`: CONLL-2000 veri kümesini kullanarak HMM ile kelime etiketleme uygular. Gerçek veri üzerinde HMM uygulaması örneğidir.
- `4_maximum_entropy.ipynb`: Maksimum Entropi (MaxEnt) modeli ile kelimelerin olasılıklarını tahmin eder. POS etiketleme ve sınıflandırma gibi görevlerde tercih edilir.

---

## Konsept Tanımları

### N-Gram Modeli
Dil modellemede, bir kelimenin yalnızca önceki \(n-1\) kelimeye bağlı olduğunu varsayan istatistiksel bir modeldir. N sayısı arttıkça bağlam artar, ancak veri ihtiyacı da büyür.

### Gizli Markov Modeli (HMM)
Gözlemlenen çıktılar (kelimeler) ile gözlemlenemeyen durumlar (örneğin POS etiketleri) arasında olasılıksal ilişkiler kurar. Zincirleme bir yapıya sahiptir.

### Maksimum Entropi Modeli (MaxEnt)
Hiçbir gereksiz varsayım yapmadan, mevcut verilere maksimum belirsizlik (entropi) ile uyan en uygun olasılık dağılımını bulur. Özellik temelli bir modeldir.

---
