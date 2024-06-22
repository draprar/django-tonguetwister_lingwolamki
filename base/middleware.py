from django.contrib.auth.middleware import get_user


class LoginStreakMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = get_user(request)
        if user.is_authenticated:
            profile = user.profile
            if profile.login_streak is None:
                profile.login_streak = 1
            else:
                profile.login_streak += 1
            profile.save()
        response = self.get_response(request)
        return response
