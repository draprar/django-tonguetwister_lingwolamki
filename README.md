# 🎤 LingwoŁamki — Django App (Archived)

LingwoŁamki is a Django web application designed to help users improve vocal clarity, articulation, and breathing techniques. It includes tongue twisters, exercises, trivia, fun facts, and more — all manageable through an admin panel and presented through a responsive frontend.

> ⚠️ This repository is archived.  
> This project has been integrated into my main portfolio:  
> https://github.com/draprar/django_portfolio-walery (see `/tonguetwister` app)

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

- **User Login Streak Tracking**: Tracks daily user login streaks and updates them automatically. Users are encouraged to maintain their streak.
- **Content Management**: Admin users can manage a variety of models including:
  - Tongue Twisters.
  - Articulators.
  - Exercises.
  - Trivia.
  - Funfacts.
  - Old Polish phrases.
- **Dynamic Typography Handling**: Automatically adjusts typographic elements to ensure proper formatting, particularly for the Polish language (e.g., preventing single-letter words like "i" at the end of lines).
- **Email Notifications**: 
  - Account activation emails for new users.
  - Password reset emails with secure token-based links.
  - Contact form submissions sent directly to the admin's email.
- **Authentication**: 
  - User registration with email confirmation.
  - Login/logout functionality.
  - Password reset functionality.
- **Responsive Design**: Optimized for both desktop and mobile views, providing a seamless experience across different devices.
- **Polish Language Support**: Fully localized for Polish-speaking users, from UI to error messages and notifications.

## 🛠️ Tech Stack

- Python 3.10+  
- Django 4.2.1  
- SQLite (default) or MySQL  
- `django-environ` for environment variables  
- WhiteNoise for static files  

## ⚡ Installation

### Step-by-Step Guide

1. **Clone the repository:**

Via:

```bash
git clone https://github.com/draprar/django-tonguetwister-app_lingwolamki.git
cd lingwolamki
```

2. **Install dependencies:**

Make sure you have `pip` installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

Create a `.env` file in the project root directory with the following keys:

   ```bash
   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=your-allowed-hosts
   EMAIL_HOST=smtp.your-email-provider.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your-email@example.com
   EMAIL_HOST_PASSWORD=your-email-password
   DEFAULT_FROM_EMAIL=your-email@example.com
   USE_MYSQL=False
   ```

4. **Apply migrations:**

Run the following command to apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

To access the admin panel, create a superuser with the command:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

Start the Django development server:

   ```bash
   python manage.py runserver
   ```
7. **Access the app:**

- Main page: `/`
- Admin panel: `http://127.0.0.1:8000/admin/`

## 🌿 Project Structure

```tree
lingwolamki/
│
├── base/
│   ├── __init__.py
│   ├── settings.py       # Configuration settings for the Django project
│   ├── urls.py           # URL routing for the project
│   ├── wsgi.py           # WSGI configuration for deployment
│   ├── middleware.py     # Custom middleware for tracking user login streaks
│
├── tonguetwister/
│   ├── __init__.py
│   ├── apps.py           # App configuration for TongueTwister
│   ├── models.py         # Database models (Twister, Articulator, etc.)
│   ├── views.py          # Views for handling frontend interaction
│   ├── urls.py           # URL routing for TongueTwister
│   ├── templates/        # HTML templates for the app
│
├── static/               # Static files (CSS, JavaScript, Images)
├── media/                # User-uploaded media files
├── db.sqlite3            # SQLite database (used for development)
├── .env                  # Environment variables
└── manage.py             # Django project management script
```

## 📌 Notes

- This project is no longer actively maintained as a standalone app.
- The tongue-twister functionality now lives inside the main portfolio project.
- This repository is kept as an archived reference.

## 📜 License
This project is licensed under the MIT License.

## 👤 Authors
Developed by ***Michał*** & ***Paulina***.
