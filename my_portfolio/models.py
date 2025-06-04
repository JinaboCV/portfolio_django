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
    
class Project(models.Model):
    name = models.CharField(max_length=150)
    description = RichTextField()
    
class BlogPostCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.CharField(max_length=255)
    """ deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) """

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    category = models.ForeignKey(BlogPostCategory, on_delete=models.SET_NULL, null=True, blank= True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    thumbnail = models.ImageField(upload_to='articles/thumbnails/', height_field=None, width_field=None, max_length=None)
    content = RichTextField()
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def read_time(self):
        return calculate_read_time(self.content)
    
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email