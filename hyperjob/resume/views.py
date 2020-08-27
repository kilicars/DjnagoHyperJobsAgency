from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

from .models import Resume


# Create your views here.
class ResumeListView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        context = {"resumes": resumes}
        return render(request, "resume/index.html", context=context)


class CreateResumeView(View):
    def get(self, request):
        return render(request, "resume/create.html")

    def post(self, request):
        if request.user.is_authenticated and not request.user.is_staff:
            description = request.POST.get("description")
            author = request.user
            Resume.objects.create(description=description, author=author)
            return redirect("/home")
        else:
            return HttpResponse(status=403)
