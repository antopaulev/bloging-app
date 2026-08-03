from django.shortcuts import redirect, render

from blogs.models import Blog, Category, About
from .forms import RegistrationForm


def home(request):
     featured_posts = Blog.objects.filter(is_featured = True , status = 'Published').order_by('updated_at')
     posts = Blog.objects.filter(is_featured = False, status = 'Published')

     try:
          about = About.objects.get()
     except:
          return None
     context = {
          'featured_posts': featured_posts,
          'posts' : posts,
          'about' : about,
     }
     return render(request, 'home.html' , context )

def register(request):
     if request.method == 'POST':
          form = RegistrationForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('home')

     else:
          form = RegistrationForm()
     context = {
          'form': form,
     }
     return render(request, 'register.html', context)