from datetime import timedelta
from django.contrib.auth.middleware import get_user
from django.utils import timezone


class LoginStreakMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = get_user(request)
        if user.is_authenticated:
            profile = user.profile
            today = timezone.now().date()

            if profile.last_login_date == today:
                pass
            else:
                if profile.last_login_date == today - timedelta(days=1):
                    profile.login_streak += 1
                else:
                    profile.login_streak = 1

                profile.last_login_date = today
                profile.save()
        response = self.get_response(request)
        return response
