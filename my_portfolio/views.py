from django.shortcuts import render

def index(request):
    
    return render(request, 'my_portfolio/index.html')

def blogs(request):
    
    return render(request, 'my_portfolio/blog.html')

def blog_post(request):
    return render(request, 'my_portfolio/blog_post.html')
# Create your views here.
