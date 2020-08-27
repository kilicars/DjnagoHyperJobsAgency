from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from resume.models import Resume
from vacancy.models import Vacancy


# Create your views here.
class MainMenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "hyperjob/index.html")


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = "login"
    template_name = "hyperjob/signup.html"


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'hyperjob/login.html'


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        is_manager = False
        resumes = []
        vacancies = []

        if request.user.is_authenticated:
            is_manager = request.user.is_staff
            resumes = Resume.objects.filter(author=request.user)
            vacancies = Vacancy.objects.filter(author=request.user)

        context = {"is_manager": is_manager, "resumes": resumes, "vacancies": vacancies}
        return render(request, "hyperjob/profile.html", context=context)
