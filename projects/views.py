from django.shortcuts import render
from projects.models import Project


# Create your views here.
def project_list(request):
    available_projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {"project_list": available_projects})
