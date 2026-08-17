from django import forms
from blogs.models import Blog,Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','category','featured_image','short_discription','blog_body','status','is_featured')


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','groups','is_staff', 'is_active')