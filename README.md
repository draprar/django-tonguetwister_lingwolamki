![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-4.2+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 🎤 LingwoŁamki — Django App (Archived)

A Django app for improving vocal clarity, articulation, and breathing techniques.
Tongue twisters, exercises, trivia, fun facts, and old Polish phrases — all manageable through an admin panel and presented through a responsive frontend.

> ⚠️ This repository is archived.  
> This project has been integrated into my main portfolio:  
> https://github.com/draprar/django_portfolio-walery (see `/tonguetwister` app)

> 🌐 Live version: https://walery.site/tonguetwister/

![Project Demo](tonguetwister/static/assets/ll-demo.gif)

## 📖 Overview

This application was built as a standalone Django project focused on speech-training tools, gamified practice, and content-rich UI.

It has since been integrated into the main portfolio project as a compact, modular tongue-twister app.

## 🧠 Project Evolution

- Standalone Django application  
- Feature-rich content system (twisters, exercises, trivia, funfacts, old Polish phrases)  
- Integrated into the portfolio project as a module  
- Archived for historical reference
  
## ✨ Features

- **Login Streak Tracking**
  - Tracks daily user login streaks and updates them automatically
- **Content Management**
  - Tongue Twisters, Articulators, Exercises, Trivia, Funfacts, Old Polish phrases
- **Dynamic Typography**
  - Automatically adjusts formatting for Polish language conventions
- **Email Notifications**
  - Account activation, password reset, and contact form emails
- **Authentication**
  - Registration with email confirmation, login/logout, password reset
- **Responsive Design**
  - Optimized for desktop and mobile views
- **Polish Language Support**
  - Fully localized UI, error messages, and notifications

## 🚀 Installation

### Requirements

- Python 3.10+
- Django 4.2+
- SQLite (default) or MySQL for production
- `django-environ` for environment variable management
- WhiteNoise for static files

### Step-by-Step Guide

1. **Clone the repository**:
```
   git clone https://github.com/draprar/django-tonguetwister-app_lingwolamki.git
   cd lingwolamki
```

2. **Create and activate a virtual environment**:
```
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```
   pip install -r requirements.txt
```

4. **Set up environment variables**:
Create a `.env` file in the project root directory and add the following:
```
   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   EMAIL_HOST=smtp.your-email-provider.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your-email@example.com
   EMAIL_HOST_PASSWORD=your-email-password
   DEFAULT_FROM_EMAIL=your-email@example.com
   USE_MYSQL=False
```

5. **Apply migrations**:
```
   python manage.py makemigrations
   python manage.py migrate
```

6. **Create a superuser**:
```
   python manage.py createsuperuser
```

7. **Run the development server**:
```
   python manage.py runserver
```

8. **Access the application**:
   - Main page: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📜 License

This project is licensed under the MIT License.

## 👤 Authors

Developed by ***Michał*** & ***Paulina***.
