# 🧩 Норматив 4 — Django REST API + Telegram Bot

Проект демонстрирует интеграцию **Django REST Framework** и **Telegram-бота** на **Aiogram 3**, где бот получает и фильтрует данные через **aiohttp**-запросы к API.

---

## 🚀 Цель
Создать Telegram-бота, который:
- получает данные о курсах из Django REST API,  
- автоматически фильтрует их по введённому пользователем запросу:  
  - число → фильтрация по `id__gte`,  
  - текст → поиск по `title__icontains`.

---

## ⚙️ Используемые технологии
- **Python 3.10+**
- **Django & Django REST Framework**
- **Aiogram 3**
- **Aiohttp**
- **SQLite (по умолчанию)**

---

## 🚀 Установка и запуск

### 1️⃣ Клонирование репозитория
- git clone https://github.com/<твой_профиль>/<название_репозитория>.git
- cd <название_репозитория>
  
### 2️⃣ Установка зависимостей
- pip install -r requirements.txt
- pip install django djangorestframework aiogram aiohttp
  
### 3️⃣ Настройка Django
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
  
API будет доступен по адресу:
- 👉 http://127.0.0.1:8000/api/courses/

### 4️⃣ Настройка Telegram-бота
- Создай бота через @BotFather
- Получи TOKEN
- Укажи его в файле bot_api.py:
  
python

- TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
- API_URL = "http://127.0.0.1:8000/api/users/"
  
### 5️⃣ Запуск бота
- python bot_api.py
- 💬 Команды бота
  
- /start	Регистрирует пользователя в базе (отправляет POST на Django API)
- Патом в баре появится кнопки

## 🗂 Структура проекта

- project/
- │
- ├── core/
- │   ├── models.py        # Модель BotUser
- │   ├── serializers.py   # Сериализация модели
- │   ├── views.py         # ViewSet для REST API
- │   ├── urls.py          # Маршруты API
- │   ├── filters.py       # Фильтрация через django-filters
- ├── bot_api.py           # Код Telegram-бота (Aiogram + aiohttp)
- │
- ├── manage.py
- └── requirements.txt

--- 

## 🧠 Принцип работы
###Этап	Что делает

1	Пользователь отправляет команду /start

2 Бот делает GET-запрос к API /api/courses/

3 Django возвращает список курсов (JSON)

4 Филтирация 
- 📚 Доступные курсы:
- • Django — ID: 1
- • Python — ID: 2
- • SQL — ID: 3

🔎 Чтобы найти курс:
— просто введите номер ID (например: 2)
— или часть названия (например: python)



## 🛠 Пример работы бота

<img width="1172" height="645" alt="image" src="https://github.com/user-attachments/assets/236cc2e5-5e32-46bf-bddb-1f4ee865ee45" />

<img width="928" height="522" alt="image" src="https://github.com/user-attachments/assets/bf3bfa89-f97a-430f-884c-449524c2067f" />

<img width="928" height="513" alt="image" src="https://github.com/user-attachments/assets/220fac43-d37b-4080-8973-8c9d3f0a2a37" />

📄 Лицензия
Свободное использование в учебных целях.
