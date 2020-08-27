from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from .models import Vacancy


# Create your views here.
class VacancyListView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        context = {"vacancies": vacancies}
        return render(request, "vacancy/index.html", context=context)


class CreateVacancyView(View):
    def get(self, request):
        return render(request, "vacancy/create.html")

    def post(self, request):
        if request.user.is_authenticated and request.user.is_staff:
            description = request.POST.get("description")
            author = request.user
            Vacancy.objects.create(description=description, author=author)
            return redirect("/home")
        else:
            return HttpResponse(status=403)
