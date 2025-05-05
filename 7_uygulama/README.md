# Chatbot ile Sohbet Uygulaması

Bu proje, OpenAI GPT-3.5-turbo modelini kullanarak basit bir sohbet botu oluşturmayı amaçlar. Kullanıcı ile etkileşimli bir sohbet ortamı sağlar. Kullanıcıdan alınan mesajlar, modelin yanıtlarını üretmek için kullanılır ve her iki tarafın konuşmaları bir geçmiş listesinde saklanır.

---

## Dosya ve Açıklamaları

- `chatbot.py`: OpenAI API'sini kullanarak çalışan sohbet botunun Python kodunu içerir. Kullanıcıdan gelen mesajlar API'ye gönderilir ve yanıt alınarak ekrana yazdırılır.

---

## Konsept Tanımları

### Chatbot Nedir?
Chatbot, kullanıcı ile doğal dilde etkileşimde bulunan yazılım uygulamalarıdır. Çoğu chatbot, kullanıcıların sorularını yanıtlayabilen veya belirli görevleri yerine getirebilen sistemlerdir. Bu proje, OpenAI GPT-3.5-turbo modelini kullanarak gelişmiş bir sohbet deneyimi sunar.

### OpenAI API
OpenAI, yapay zeka tabanlı dil modelleri geliştiren bir şirkettir. Bu proje, OpenAI'nin GPT-3.5-turbo modelini kullanarak sohbet botları oluşturmak için API'yi kullanmaktadır. API, geliştiricilerin doğal dil işleme (NLP) görevlerini çözmelerine yardımcı olur.

---

# OpenAI API Anahtarı ve `.env` Dosyasının Kullanımı

Bu proje, OpenAI API anahtarını güvenli bir şekilde kullanmak için `.env` dosyasını kullanır. Bu dosya, API anahtarınızı içerir ve uygulamanızın çalışma zamanı sırasında otomatik olarak yüklenir. Aşağıdaki adımları izleyerek `.env` dosyasını ve OpenAI API anahtarınızı doğru şekilde ayarlayabilirsiniz.

### Adım 1: OpenAI API Anahtarını Alın

1. [OpenAI API](https://platform.openai.com/signup) sayfasına gidin.
2. Hesabınızı oluşturun veya mevcut hesabınıza giriş yapın.
3. "API Key" bölümünden yeni bir API anahtarı oluşturun.
4. API anahtarınızı kopyalayın.

### Adım 2: `.env` Dosyasını Oluşturun

1. Proje klasörünüzde `.env` isminde bir dosya oluşturun (dosya adı tam olarak `.env` olmalıdır).
2. `.env` dosyasına şu satırı ekleyin:

```plaintext
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

## Gereksinimler

- Python 3.x
- `openai` ve `python-dotenv` paketleri (API'yi kullanabilmek için)

Aşağıdaki komutlarla gerekli paketleri yükleyebilirsiniz:

```bash
pip install openai python-dotenv