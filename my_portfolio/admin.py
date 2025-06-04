from django.contrib import admin
from .models import Achievements, Experience, Project, Service, ServiceCategory, Skill, SkillCategory, Task, BlogPostCategory, BlogPost, Subscriber 


    
class AdminSkillCategory(admin.ModelAdmin):
    list_display = ['name']
    
class AdminSkill(admin.ModelAdmin):
    list_display = ('name', 'percentage')
    
class AdminServiceCategory(admin.ModelAdmin):
    list_display = ['name']
    
class AdminService(admin.ModelAdmin):
    list_display = ['name']

class AdminExperience(admin.ModelAdmin):
    list_display = ('title', 'company')
    
class AdminAchievements(admin.ModelAdmin):
    list_display = ('title_archieved', 'year')
    
class AdminTask(admin.ModelAdmin):
    list_display = ['description']
    
class AdminProjects(admin.ModelAdmin):
    list_display = ['name']

class AdminBlogPostCategory(admin.ModelAdmin):
    list_display = ['title']

class AdminBlogPost(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ('title', 'category',)

class AdminSubcriber(admin.ModelAdmin):
    list_display = ['email']    
    
    
admin.site.register(SkillCategory, AdminSkillCategory)
admin.site.register(Skill, AdminSkill)
admin.site.register(ServiceCategory, AdminServiceCategory)
admin.site.register(Service, AdminService)
admin.site.register(Experience, AdminExperience)
admin.site.register(Achievements, AdminAchievements)
admin.site.register(Task, AdminTask)
admin.site.register(Project, AdminProjects)
admin.site.register(BlogPostCategory, AdminBlogPostCategory)
admin.site.register(BlogPost, AdminBlogPost)
admin.site.register(Subscriber, AdminSubcriber)