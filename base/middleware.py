from datetime import timedelta
from django.contrib.auth.middleware import get_user
from django.utils import timezone


class LoginStreakMiddleware:
    """
    Middleware that updates the login streak of an authenticated user.
    If the user logs in on consecutive days, the streak is incremented.
    If the user misses a day, the streak is reset to 1.
    """
    def __init__(self, get_response):
        # Middleware initialization method. Receives the next callable in the stack.
        self.get_response = get_response

    def __call__(self, request):
        user = get_user(request)  # get the user from the request

        if user.is_authenticated:
            profile = user.profile  # access the user's profile
            today = timezone.now().date()

            # If the last login date is not today, update the login streak
            if profile.last_login_date != today:
                # If the last login was exactly yesterday, increment the streak
                if profile.last_login_date == today - timedelta(days=1):
                    profile.login_streak += 1
                # If more time has passed, reset the streak to 1
                else:
                    profile.login_streak = 1

                # Update the last login date to today and save the profile
                profile.last_login_date = today
                profile.save()

        # Proceed to the next middleware or view
        response = self.get_response(request)
        return response
