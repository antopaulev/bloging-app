from django import forms

from blogs.models import Blog, Category,User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','category','featured_image','short_discription','blog_body','status','is_featured')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password', 'is_staff', 'is_active')