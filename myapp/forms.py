from django import forms
from .models import User, Blog


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password','first_name','last_name','email']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','blog']
