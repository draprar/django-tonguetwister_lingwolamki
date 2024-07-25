from django import forms
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.template.loader import render_to_string
from .models import (Twister, Articulator, Exercise, Trivia, Funfact, UserProfileArticulator, UserProfileTwister,
                     UserProfileExercise)
from .forms import ArticulatorForm, ExerciseForm, TwisterForm, TriviaForm, FunfactForm, CustomUserCreationForm, ContactForm, AvatarUploadForm
import logging
from weasyprint import HTML


logger = logging.getLogger(__name__)


def is_admin(user):
    return user.is_staff or user.is_superuser


def main(request):
    try:
        twisters = Twister.objects.all().order_by('id')
        articulators = Articulator.objects.all()[:1]
        if request.user.is_authenticated:
            user_articulators_texts = list(
                UserProfileArticulator.objects.filter(user=request.user).values_list('articulator__text', flat=True))
        else:
            user_articulators_texts = []
        exercises = Exercise.objects.all()[:1]
        if request.user.is_authenticated:
            user_exercises_texts = list(
                UserProfileExercise.objects.filter(user=request.user).values_list('exercise__text', flat=True))
        else:
            user_exercises_texts = []
        trivia = Trivia.objects.all()[:0]
        funfacts = Funfact.objects.all()[:0]
        paginator = Paginator(twisters, 1)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        context = {'page_obj': page_obj,
                   'articulators': articulators,
                   'user_articulators_texts': user_articulators_texts,
                   'exercises': exercises,
                   'user_exercises_texts': user_exercises_texts,
                   'trivia': trivia,
                   'funfacts': funfacts,
                   }

        if request.htmx:
            return render(request, 'tonguetwister/partials/gen/list.html', context)
        return render(request, 'tonguetwister/main.html', context)

    except Exception as e:
        # Log the exception
        print(f"Exception occurred: {str(e)}")
        # Return an HttpResponse with an error message or redirect to an error page
        return HttpResponse("Internal Server Error", status=500)


def load_more_articulators(request):
    try:
        offset = int(request.GET.get('offset', 0))
        limit = 1
        articulators = Articulator.objects.all()[offset:offset + limit]

        if request.user.is_authenticated:
            user_articulators_texts = set(
                UserProfileArticulator.objects.filter(user=request.user).values_list('articulator__text', flat=True)
            )
        else:
            user_articulators_texts = set()

        data = []
        for articulator in articulators:
            is_added = articulator.text in user_articulators_texts
            data.append({
                'id': articulator.id,
                'text': articulator.text,
                'is_added': is_added,
            })

        return JsonResponse(data, safe=False)

    except Exception as e:
        print(f"Exception occurred in load_more_articulators: {str(e)}")
        return JsonResponse({'error': 'Internal Server Error'}, status=500)


def load_more_exercises(request):
    try:
        offset = int(request.GET.get('offset', 0))
        limit = 1
        exercises = Exercise.objects.all()[offset:offset + limit]

        if request.user.is_authenticated:
            user_exercises_texts = set(
                UserProfileExercise.objects.filter(user=request.user).values_list('exercise__text', flat=True)
            )
        else:
            user_exercises_texts = set()

        data = []
        for exercise in exercises:
            is_added = exercise.text in user_exercises_texts
            data.append({
                'id': exercise.id,
                'text': exercise.text,
                'is_added': is_added,
            })

        return JsonResponse(data, safe=False)

    except Exception as e:
        print(f"Exception occurred in load_more_exercises: {str(e)}")
        return JsonResponse({'error': 'Internal Server Error'}, status=500)


def load_more_trivia(request):
    offset = int(request.GET.get('offset', 0))
    limit = 1
    trivia = Trivia.objects.all()[offset:offset + limit]
    data = list(trivia.values())
    return JsonResponse(data, safe=False)


def load_more_funfacts(request):
    offset = int(request.GET.get('offset', 0))
    limit = 1
    funfacts = Funfact.objects.all()[offset:offset + limit]
    data = list(funfacts.values())
    return JsonResponse(data, safe=False)


def error_404_view(request, exception):
    data = {}
    return render(request, 'tonguetwister/404.html', data)


@user_passes_test(is_admin)
def articulator_list(request):
    articulators = Articulator.objects.all()
    return render(request, 'tonguetwister/articulators/articulator_list.html', {'articulators': articulators})


@user_passes_test(is_admin)
def articulator_add(request):
    if request.method == "POST":
        form = ArticulatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulator_list')
    else:
        form = ArticulatorForm()
    return render(request, 'tonguetwister/articulators/articulator_form.html', {'form': form})


@user_passes_test(is_admin)
def articulator_edit(request, pk):
    articulator = get_object_or_404(Articulator, pk=pk)
    if request.method == "POST":
        form = ArticulatorForm(request.POST, instance=articulator)
        if form.is_valid():
            form.save()
            return redirect('articulator_list')
    else:
        form = ArticulatorForm(instance=articulator)
    return render(request, 'tonguetwister/articulators/articulator_form.html', {'form': form})


@user_passes_test(is_admin)
def articulator_delete(request, pk):
    articulator = get_object_or_404(Articulator, pk=pk)
    if request.method == "POST":
        articulator.delete()
        return redirect('articulator_list')
    return render(request, 'tonguetwister/articulators/articulator_confirm_delete.html', {'articulator': articulator})


@user_passes_test(is_admin)
def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'tonguetwister/exercises/exercise_list.html', {'exercises': exercises})


@user_passes_test(is_admin)
def exercise_add(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    return render(request, 'tonguetwister/exercises/exercise_form.html', {'form': form})


@user_passes_test(is_admin)
def exercise_edit(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == "POST":
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'tonguetwister/exercises/exercise_form.html', {'form': form})


@user_passes_test(is_admin)
def exercise_delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == "POST":
        exercise.delete()
        return redirect('exercise_list')
    return render(request, 'tonguetwister/exercises/exercise_confirm_delete.html', {'exercise': exercise})


@user_passes_test(is_admin)
def twister_list(request):
    twisters = Twister.objects.all()
    return render(request, 'tonguetwister/twisters/twister_list.html', {'twisters': twisters})


@user_passes_test(is_admin)
def twister_add(request):
    if request.method == "POST":
        form = TwisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('twister_list')
    else:
        form = TwisterForm()
    return render(request, 'tonguetwister/twisters/twister_form.html', {'form': form})


@user_passes_test(is_admin)
def twister_edit(request, pk):
    twister = get_object_or_404(Twister, pk=pk)
    if request.method == "POST":
        form = TwisterForm(request.POST, instance=twister)
        if form.is_valid():
            form.save()
            return redirect('twister_list')
    else:
        form = TwisterForm(instance=twister)
    return render(request, 'tonguetwister/twisters/twister_form.html', {'form': form})


@user_passes_test(is_admin)
def twister_delete(request, pk):
    twister = get_object_or_404(Twister, pk=pk)
    if request.method == "POST":
        twister.delete()
        return redirect('twister_list')
    return render(request, 'tonguetwister/twisters/twister_confirm_delete.html', {'twister': twister})


@user_passes_test(is_admin)
def trivia_list(request):
    trivia = Trivia.objects.all()
    return render(request, 'tonguetwister/trivia/trivia_list.html', {'trivia': trivia})


@user_passes_test(is_admin)
def trivia_add(request):
    if request.method == "POST":
        form = TriviaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trivia_list')
    else:
        form = TriviaForm()
    return render(request, 'tonguetwister/trivia/trivia_form.html', {'form': form})


@user_passes_test(is_admin)
def trivia_edit(request, pk):
    trivia = get_object_or_404(Trivia, pk=pk)
    if request.method == "POST":
        form = TriviaForm(request.POST, instance=trivia)
        if form.is_valid():
            form.save()
            return redirect('trivia_list')
    else:
        form = TriviaForm(instance=trivia)
    return render(request, 'tonguetwister/trivia/trivia_form.html', {'form': form})


@user_passes_test(is_admin)
def trivia_delete(request, pk):
    t = get_object_or_404(Trivia, pk=pk)
    if request.method == "POST":
        t.delete()
        return redirect('trivia_list')
    return render(request, 'tonguetwister/trivia/trivia_confirm_delete.html', {'t': t})


@user_passes_test(is_admin)
def funfact_list(request):
    funfacts = Funfact.objects.all()
    return render(request, 'tonguetwister/funfacts/funfact_list.html', {'funfacts': funfacts})


@user_passes_test(is_admin)
def funfact_add(request):
    if request.method == "POST":
        form = FunfactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funfact_list')
    else:
        form = FunfactForm()
    return render(request, 'tonguetwister/funfacts/funfact_form.html', {'form': form})


@user_passes_test(is_admin)
def funfact_edit(request, pk):
    funfact = get_object_or_404(Funfact, pk=pk)
    if request.method == "POST":
        form = FunfactForm(request.POST, instance=funfact)
        if form.is_valid():
            form.save()
            return redirect('funfact_list')
    else:
        form = FunfactForm(instance=funfact)
    return render(request, 'tonguetwister/funfacts/funfact_form.html', {'form': form})


@user_passes_test(is_admin)
def funfact_delete(request, pk):
    funfact = get_object_or_404(Funfact, pk=pk)
    if request.method == "POST":
        funfact.delete()
        return redirect('funfact_list')
    return render(request, 'tonguetwister/funfacts/funfact_confirm_delete.html', {'funfact': funfact})


@login_required
def user_content(request):
    profile = request.user.profile
    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'delete-avatar':
            if profile.avatar:
                profile.avatar.delete(save=True)
                messages.success(request, 'Awatar został usunięty.')
            else:
                messages.info(request, 'Brak awatara do usunięcia.')
                return redirect('user_content')

        form = AvatarUploadForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user_content')
    else:
        form = AvatarUploadForm(instance=request.user.profile)

    all_articulators = Articulator.objects.all()
    user_articulators = UserProfileArticulator.objects.filter(user=request.user).select_related('articulator')
    user_articulators_texts = list(
        UserProfileArticulator.objects.filter(user=request.user).values_list('articulator__text', flat=True))
    all_exercises = Exercise.objects.all()
    user_exercises = UserProfileExercise.objects.filter(user=request.user).select_related('exercise')
    user_exercises_texts = list(
        UserProfileExercise.objects.filter(user=request.user).values_list('exercise__text', flat=True))
    all_twisters = Twister.objects.all()
    user_twisters = UserProfileTwister.objects.filter(user=request.user).select_related('twister')
    user_twisters_texts = list(
        UserProfileTwister.objects.filter(user=request.user).values_list('twister__text', flat=True))

    context = {
        'form': form,
        'articulators': all_articulators,
        'user_articulators': user_articulators,
        'user_articulators_texts': user_articulators_texts,
        'exercises': all_exercises,
        'user_exercises': user_exercises,
        'user_exercises_texts': user_exercises_texts,
        'all_twisters': all_twisters,
        'user_twisters': user_twisters,
        'user_twisters_texts': user_twisters_texts,
    }

    if 'export' in request.GET and request.GET['export'] == 'exercises':
        html_string = render_to_string('tonguetwister/users/export-exercises.html', context)
        html = HTML(string=html_string)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="lingwolamkowe-cwiczenia.pdf"'
        html.write_pdf(target=response)
        return response

    return render(request, 'tonguetwister/users/user-content.html', context)


@login_required
@csrf_protect
def add_articulator(request, articulator_id):
    user = request.user
    articulator = get_object_or_404(Articulator, id=articulator_id)
    if UserProfileArticulator.objects.filter(user=user, articulator=articulator).exists():
        return JsonResponse({'status': 'Duplicate articulator'})
    user_articulator = UserProfileArticulator.objects.create(user=user, articulator=articulator)
    return JsonResponse({'status': 'Articulator added', 'userArticulatorId': user_articulator.id})


@login_required
@csrf_protect
def delete_articulator(request, articulator_id):
    user = request.user
    articulator = get_object_or_404(UserProfileArticulator, id=articulator_id, user=user)
    articulator.delete()
    return JsonResponse({'status': 'Articulator deleted'})


@login_required
@csrf_protect
def add_exercise(request, exercise_id):
    user = request.user
    exercise = get_object_or_404(Exercise, id=exercise_id)
    if UserProfileExercise.objects.filter(user=user, exercise=exercise).exists():
        return JsonResponse({'status': 'Duplicate exercise'})
    user_exercise = UserProfileExercise.objects.create(user=user, exercise=exercise)
    return JsonResponse({'status': 'Exercise added', 'userExerciseId': user_exercise.id})


@login_required
@csrf_protect
def delete_exercise(request, exercise_id):
    exercise = get_object_or_404(UserProfileExercise, id=exercise_id, user=request.user)
    exercise.delete()
    return JsonResponse({'status': 'Exercise deleted'})


@login_required
@csrf_protect
def add_twister(request, twister_id):
    user = request.user
    twister = get_object_or_404(Twister, id=twister_id)
    if UserProfileTwister.objects.filter(user=user, twister=twister).exists():
        return JsonResponse({'status': 'Duplicate twister'})
    user_twister = UserProfileTwister.objects.create(user=user, twister=twister)
    return JsonResponse({'status': 'Twister added', 'userTwisterId': user_twister.id})


@login_required
@csrf_protect
def delete_twister(request, twister_id):
    twister = get_object_or_404(UserProfileTwister, id=twister_id, user=request.user)
    twister.delete()
    return JsonResponse({'status': 'Twister deleted'})


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            regular_users_group = Group.objects.get(name='Regular Users')
            user.groups.add(regular_users_group)
        return user


def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            error = 'Invalid username or password'
    return render(request, 'registration/login.html', {'error': error})


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form is valid and saved.")
            return redirect('login')
        else:
            print("Form is not valid. Errors: ", form.errors)
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        print("GET request. Rendering empty form.")
    return render(request, 'registration/register.html', {'form': form})


def info(request):
    return render(request, 'tonguetwister/partials/static/info.html')


def materials(request):
    return render(request, 'tonguetwister/partials/static/materials.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f'Kontakt od {name}'

            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Twoja wiadomość została wysłana')
            except Exception as e:
                messages.error(request, f'Błąd przy wysyłaniu wiadomości: {e}')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'tonguetwister/partials/static/contact.html', {'form': form})
