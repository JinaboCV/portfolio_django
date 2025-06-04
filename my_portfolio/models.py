from django.db import models
from ckeditor.fields import RichTextField

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.CharField(max_length=3)
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
    
class Project(models.Model):
    name = models.CharField(max_length=150)
    description = RichTextField()

