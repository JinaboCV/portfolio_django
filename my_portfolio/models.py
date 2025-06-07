from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from .utils import calculate_read_time

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()
    category = models.ForeignKey(SkillCategory, on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.name
    
class ServiceCategory(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(ServiceCategory, on_delete=models.RESTRICT, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    startedAt = models.CharField(max_length=15)
    endAt = models.CharField(max_length=15)
    
    def __str__(self):
        return self.title + ' ' + self.company
     
class Task(models.Model):
    description = models.TextField(blank=True)
    experience = models.ForeignKey(Experience, on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.description
    
class Achievements(models.Model):
    title_archieved = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    year = models.IntegerField()
    
    def __str__(self):
        return self.title_archieved + ' ' + self.year

class Status(models.TextChoices):
    PENDING = 'PEN', 'Pending'
    LINK = 'LIN', 'Link'
    HOLD = 'HLD', 'Holding'
        
class Project(models.Model):
    name = models.CharField(max_length=150)
    description = RichTextField()
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.PENDING)
    
class ContactMsg(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.email}"