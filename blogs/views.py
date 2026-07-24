from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404 
from . models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status = 'Published' , category = category_id)
    #use try/catch if i want to use custom method for handling error and redirect it to home page
    try:
        category = Category.objects.get(pk = category_id)
    except:
        return redirect('home')
    # use this if i want to show 404 default page if the object is not found
    # category = get_object_or_404(Category, pk = category_id)
    context = {
        'posts' : posts,
        'category': category,
    }
    return render(request, "post_by_category.html", context)