from django.shortcuts import render
from .models import SkillCategory, Skill, Service, Achievements, BlogPost, ServiceCategory

def index(request):
    frontend_skills=    Skill.objects.filter(category__name = 'Frontend')
    backend_skills=    Skill.objects.filter(category__name = 'Backend')
    other_skills = Skill.objects.filter(category__name = 'Tool & Others') 
    
    service_category = ServiceCategory.objects.all()
    context = {
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'other_skills': other_skills,
        'service_category' : service_category
        }
    return render(request, 'my_portfolio/index.html', context=context)

def blogs(request):
    
    return render(request, 'my_portfolio/blog.html')

def blog_post(request):
    return render(request, 'my_portfolio/blog_post.html')
# Create your views here.
