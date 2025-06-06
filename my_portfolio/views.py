from django.shortcuts import render
from .models import SkillCategory, Skill, Service, Achievements, BlogPost, ServiceCategory, Experience, Task

def index(request):
    skill_category = SkillCategory.objects.all()
    skills = Skill.objects.all()
    service_category = ServiceCategory.objects.all()
    
    experiences = Experience.objects.all()
    tasks = Task.objects.all()
    context = {
        'skill_category': skill_category,
        'skills': skills,
        'service_category' : service_category,
        'experiences': experiences,
        'tasks': tasks
        }
    return render(request, 'my_portfolio/index.html', context=context)

def blogs(request):
    
    return render(request, 'my_portfolio/blog.html')

def blog_post(request):
    return render(request, 'my_portfolio/blog_post.html')
# Create your views here.
