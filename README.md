**Book API - Readme**

# 📚 Book API

**Book API** — Django REST Framework (DRF) yordamida yaratilgan kitoblarni boshqarish API. Bu API orqali siz kitoblarni qo'shish, tahrirlash, o'chirish va ro'yxatini olish imkoniyatlariga ega bo'lasiz. Kitoblar bilan ishlashni oson va samarali qilish uchun ishlab chiqilgan.

---

## 🚀 Xususiyatlar

- **Kitoblar ro'yxatini olish**  
  Kitoblar haqida ma'lumotlarni (nomi, muallifi, nashriyoti va janri) olish.

- **Yangi kitob qo'shish**  
  Kitob nomi, muallif, nashriyoti va janrini belgilab, yangi kitob qo'shish.

- **Kitobni yangilash**  
  Mavjud kitob haqida ma'lumotlarni yangilash.

- **Kitobni o'chirish**  
  Keraksiz kitoblarni ro'yxatdan o'chirish.

---

## 🛠️ Texnik Talablar

- Python 3.12
- Django 5.3
- Django REST Framework (DRF)
- PostgreSQL
  
---

## ⚙️ API Foydalanish

### 1. Kitoblar ro'yxatini olish
**GET** `127.0.0.1:8000/books/`

### 2. Yangi kitob qo'shish
**POST** `127.0.0.1:8000/books/`
- Request body:
```json
{
  "title": "Kitob nomi",
  "author": "Muallif",
  "publisher": "Nashriyot",
  "genre": "Janr"
}
```

### 3. Kitobni yangilash
**PUT** `127.0.0.1:8000/books/{id}/`
- Request body:
```json
{
  "title": "Yangilangan kitob nomi",
  "author": "Yangilangan muallif",
  "publisher": "Yangilangan nashriyot",
  "genre": "Yangilangan janr"
}
```

### 4. Kitobni o'chirish
**DELETE** `127.0.0.1:8000/books/{id}/`

---

## 📥 O'rnatish

1. **Repository'ni klonlash:**
```bash
git clone https://github.com/theMirmakhmudov/DjangoBaseRestAPI.git
```

2. **Virtual muhiti yaratish:**
```bash
python -m venv .venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. **Zaruriy kutubxonalarni o'rnatish:**
```bash
pip install -r requirements.txt
```

4. **Ma'lumotlar bazasini migratsiya qilish:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Serverni ishga tushurish:**
```bash
python manage.py runserver
```


**Book API** — Kitoblarni boshqarishni osonlashtirish va modernizatsiya qilish uchun yaratilgan API. Django REST Framework asosida ishlab chiqilgan.
