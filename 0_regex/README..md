# Python Regex (re Modülü) Bilgi Notları

Bu döküman, Python'da `re` modülü kullanılarak düzenli ifadelerin nasıl kullanılacağını açıklar.

## İçerik Başlıkları

### 1. Regex Nedir?
Regex (Regular Expression), metin içinde kalıpları tanımlamak, aramak ve değiştirmek için kullanılan yapıdır.

### 2. Temel Fonksiyonlar
- `search()`: Metin içinde ilk eşleşmeyi bulur.
- `findall()`: Tüm eşleşmeleri döner.
- `match()`: Metnin sadece başıyla eşleşir.
- `sub()`: Eşleşen metinleri değiştirir.
- `fullmatch()`: Metnin tamamının desene uyup uymadığını kontrol eder.

### 3. Karakter Sınıfları
- `\d`, `\D`: Rakam ve rakam olmayan karakterler
- `\w`, `\W`: Kelime karakterleri ve olmayanlar
- `\s`, `\S`: Boşluk karakterleri ve olmayanlar

### 4. Metin Başlangıcı ve Bitişi
- `^`: Metin başlangıcı
- `$`: Metin sonu

### 5. Özel Karakterler ve Kaçış
- Özel karakterlerin (`.`, `*`, `?`, `+`, `|`, `(`, `)`, `[`, `]`, `{`, `}`, `\`) anlamlarını anlatır ve nasıl kaçış yapılacağını gösterir.

### 6. Tekrar Operatörleri
- `*`, `+`, `?`, `{m,n}`: Bir karakterin kaç kez tekrar ettiğini tanımlar.

### 7. Gruplama ve Alt Gruplar
- Parantez kullanılarak gruplar oluşturma ve her grubun ayrı ayrı yakalanması.

### 8. Karakter Kümeleri
- `[abc]`, `[^abc]`: Belirli karakterleri ya da hariç olanları tanımlama

### 9. Metin Temizleme
- Belirli karakterleri silme, sadeleştirme işlemleri.

### 10. Email ve Telefon Doğrulama
- Regex kullanarak e-posta ve telefon numarası gibi desenleri doğrulama.

### 11. İleri Seviye Konular (Opsiyonel)
- Lookahead / Lookbehind ifadeleri
- Named groups
- Flags kullanımı (örneğin `re.IGNORECASE`)

---
