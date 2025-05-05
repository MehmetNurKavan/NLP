import re

print("\n=== 1. TEMEL EŞLEŞME ===")

text = "Merhaba, benim adım Ahmet ve numaram 05321234567."
match = re.search(r"05\d{9}", text)  # 05 ile başlayan 11 haneli numara
if match:
    print("Bulunan telefon numarası:", match.group())

print("\n=== 2. TÜM EŞLEŞMELER - findall() ===")

text2 = "Ali 23 yaşında, Ayşe 30 yaşında, Veli 45 yaşında."
yaslar = re.findall(r"\d+", text2)
print("Yaşlar:", yaslar)

print("\n=== 3. METİN TEMİZLEME - sub() ===")

raw_text = "Bu bir test!!! 1234 :)"
cleaned = re.sub(r"[^a-zA-ZçğıöşüÇĞİÖŞÜ\s]", "", raw_text)
print("Temiz metin:", cleaned)

print("\n=== 4. GRUPLAMA VE ALT GRUPLAR ===")

email_text = "İletişim: ad.soyad@example.com"
email_pattern = r"([\w\.-]+)@([\w\.-]+)"
match = re.search(email_pattern, email_text)
if match:
    print("Kullanıcı adı:", match.group(1))
    print("Alan adı:", match.group(2))

print("\n=== 5. BAŞLANGIÇ VE BİTİŞ KARAKTERLERİ (^ ve $) ===")

sentence = "Merhaba dünya"
if re.match(r"^Merhaba", sentence):
    print("Cümle 'Merhaba' ile başlıyor.")
if re.search(r"dünya$", sentence):
    print("Cümle 'dünya' ile bitiyor.")

print("\n=== 6. ÖZEL KARAKTERLERİ EŞLEŞTİRME ===")

text3 = "Fiyat: 100.50 TL"
fiyat = re.findall(r"\d+\.\d+", text3)
print("Fiyatlar:", fiyat)

print("\n=== 7. BOŞLUKLARI SADELEŞTİRME ===")

text4 = "Bu     bir     test     yazısıdır."
tek_bosluk = re.sub(r"\s+", " ", text4)
print("Boşluklar düzeltilmiş:", tek_bosluk)

print("\n=== 8. KARAKTER SINIFLARI ===")

karakter_test = "abc_123 ABC!"
sonuc = re.findall(r"\w+", karakter_test)
print("Karakter sınıfı ile eşleşenler:", sonuc)

print("\n=== 9. ÖZEL KARAKTER SINIFLARI ===")

print(re.findall(r"\d+", "Yaş: 24, yıl: 2025"))  # rakamlar
print(re.findall(r"\w+", "abc_123!?"))           # harf, rakam, alt çizgi
print(re.findall(r"\S+", "Bu bir test"))         # boşluk olmayan gruplar

print("\n=== 10. TEKRAR OPERATÖRLERİ ===")

print(re.findall(r"bo*", "boooook bok b"))       # *: 0 veya daha fazla
print(re.findall(r"bo+", "boooook bok b"))       # +: 1 veya daha fazla
print(re.findall(r"bo?", "boooook bok b"))       # ?: 0 ya da 1
print(re.findall(r"\d{2,4}", "1 12 123 1234 12345"))  # {min,max}

print("\n=== 11. BİRDEN FAZLA EMAIL YAKALAMA ===")

metin = "İletişim için: ali.kara@gmail.com veya ayse_yilmaz@yahoo.com"
pattern = r"([\w\.-]+)@([\w\.-]+)"
eslesmeler = re.findall(pattern, metin)
for kullanici, alan in eslesmeler:
    print("Kullanıcı:", kullanici, "| Alan adı:", alan)

print("\n=== 12. ALT GRUPLARI YAKALAMA ===")

metin = "Ad: Ahmet, Yaş: 23"
match = re.search(r"Ad: (\w+), Yaş: (\d+)", metin)
if match:
    print("Ad:", match.group(1))
    print("Yaş:", match.group(2))

print("\n=== 13. PLAKA EŞLEŞMESİ ===")

plaka_metin = "Araba plakaları: 34ABC123, 06XYZ456"
plakalar = re.findall(r"\d{2}[A-Z]{3}\d{3}", plaka_metin)
print("Plakalar:", plakalar)

print("\n=== 14. EMAIL DOĞRULAMA ===")

emails = ["test@example.com", "yanlis@mail", "ali.k@site.co"]
for e in emails:
    if re.fullmatch(r"[\w\.-]+@[\w\.-]+\.\w{2,}", e):
        print(f"Geçerli: {e}")
    else:
        print(f"Geçersiz: {e}")
