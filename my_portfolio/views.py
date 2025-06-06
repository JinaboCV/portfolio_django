from django.shortcuts import render
from .models import SkillCategory, Skill, Service, Achievements, BlogPost, ServiceCategory

def index(request):
    frontend_skills=    Skill.objects.filter(category__name = 'Frontend')
    backend_skills=    Skill.objects.filter(category__name = 'Backend')
    other_skills = Skill.objects.filter(category__name = 'Tool & Others') 
    
    services = ServiceCategory.objects.all()
    webdev_services = Service.objects.filter(category__name = 'Web Development')
    mobiledev_services = Service.objects.filter(category__name = 'Mobile Development')
    api_services = Service.objects.filter(category__name = 'API Development')
    consulting_services = Service.objects.filter(category__name = "IT & Technical Consulting")
    desktopdev_services = Service.objects.filter(category__name = "	Desktop Application Development")
    context = {
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'other_skills': other_skills,
        'services': services,
        'webdev_services': webdev_services,
        'mobiledev_services': mobiledev_services,
        'api_services': api_services,
        'consulting_services': consulting_services,
        'desktopdev_services': desktopdev_services
        }
    return render(request, 'my_portfolio/index.html', context=context)

def blogs(request):
    
    return render(request, 'my_portfolio/blog.html')

def blog_post(request):
    return render(request, 'my_portfolio/blog_post.html')
# Create your views here.
