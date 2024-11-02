# LingwoŁamki

LingwoŁamki is a Django web application designed to help users enhance their vocal clarity, articulation, and breathing techniques. The app includes interactive features such as tongue twisters, exercises, trivia, and more to assist users in their practice. It is built using Django 4.2.1 and offers both an admin panel for content management and a front-end interface for user interaction.

![Project Demo](tonguetwister/static/assets/ll-demo.gif)

## Features

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

## Installation

### Requirements

- Python 3.10+
- Django 4.2.1
- SQLite (default) or MySQL for production
- `django-environ` package for environment variable management
- WhiteNoise for static file management

### Step-by-Step Guide

1. **Clone the repository:**

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

### Project Structure
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

### License
This project is licensed under the MIT License.

Developed by ***Michał*** & ***Paulina***.