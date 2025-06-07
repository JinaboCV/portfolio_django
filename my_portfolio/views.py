from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import SkillCategory, Skill, Service, Achievements, ServiceCategory, Experience, Task, ContactMsg

def index(request):
    skill_category = SkillCategory.objects.all()
    skills = Skill.objects.all()
    service_category = ServiceCategory.objects.all()
    services = Service.objects.all()
    experiences = Experience.objects.all()
    tasks = Task.objects.all()
    
    # sending and email
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        whatsapp = request.POST.get('whatsapp', '')
        message = request.POST['message']
        
        if name and email and whatsapp and message:
            # Storing to the database
            ContactMsg.objects.create(name=name, email=email, whatsapp=whatsapp, message= message)
            
            #Sends mail the me 
            full_msg = f"From: {name} <{email}>\n Whatsapp Numner: {whatsapp} \n\nMessage:\n{message}"
            send_mail(
                subject="Message From Portfolio",
                message= full_msg,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list= ["jinabocv@gmail.com"]
            )
            messages.success(request, '👏👏👏 Thank you for reaching out !!!')
            redirect('home')
        else:
            messages.error(request, 'Please fill in all fields.')
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
