from django import forms
from django.forms import fields
from blogapp.models import Blog


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body','blog_img']



class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body','blog_img']