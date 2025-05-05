from openai import OpenAI
from dotenv import load_dotenv
import os

# API istemcisi
# aynı dosya yolunda olan .env dosyasına OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx yerine kendi anahtarınızı yaziniz(tek satır ve boşluksuz) . daha güvenli olur
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Konuşma geçmişi
history_list = []

def chat_with_gpt(prompt):
    try:
        # Kullanıcı mesajını geçmişe ekle
        history_list.append({"role": "user", "content": prompt})

        # API'den yanıt al
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=history_list
        )

        # Asistan cevabını al
        reply = response.choices[0].message.content.strip()

        # Asistan mesajını geçmişe ekle
        history_list.append({"role": "assistant", "content": reply})

        return reply

    except Exception as e:
        return f"Hata oluştu: {str(e)}"


# Ana döngü
if __name__ == "__main__":
    while True:
        user_input = input("Kullanıcı tarafından girilen mesaj: ")

        if user_input.lower() in ["exit", "q"]:
            print("Konuşma sonlandırıldı.")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
