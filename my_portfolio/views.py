from django.shortcuts import render
from .models import SkillCategory, Skill, Service, Achievements, ServiceCategory, Experience, Task

def index(request):
    skill_category = SkillCategory.objects.all()
    skills = Skill.objects.all()
    service_category = ServiceCategory.objects.all()
    services = Service.objects.all()
    experiences = Experience.objects.all()
    tasks = Task.objects.all()
    context = {
        'skill_category': skill_category,
        'skills': skills,
        'service_category' : service_category,
        'services': services,
        'experiences': experiences,
        'tasks': tasks
        }
    return render(request, 'my_portfolio/index.html', context=context)

# Create your views here.
