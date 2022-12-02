from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from blogapp.models import Blog
from blogapp.forms import CreateBlogForm, UpdateBlogForm
from django.http import Http404
from django.contrib.auth.decorators import login_required


def user_register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request , "blogapp/user_register.html" , {"form" : form})

@login_required
def blog_list_view(request):
    blogs = Blog.objects.all()
    return render(request , "blogapp/index.html", {"blogs" : blogs})

@login_required
def get_blogs_by_id(request , id):
    obj = Blog.objects.get(pk = id)
    return render(request, "blogapp/get_blog.html", {'obj': obj})

@login_required
def create_blog_post(request):
    #print(request.user)
    form = CreateBlogForm()
    if request.method == 'POST':
        form = CreateBlogForm(request.POST , request.FILES)
        if form.is_valid():
            form = form.save(commit=False) #save method will return instance of object
            form.user = request.user  #by using request.user we will get logged in user
            form.save()
            return redirect("/blogs/blogs-list/")

    return render(request, "blogapp/add_blog.html", {"form" : form})

@login_required
def update_blog_post(request, id):
    try:
        obj = Blog.objects.get(pk = id)
        form = UpdateBlogForm(instance = obj)

        if request.method == 'POST':
            form = UpdateBlogForm(request.POST , request.FILES, instance = obj)
            if form.is_valid():
                form.save()
                return redirect("/blogs/blogs-list/")

        context = {
            'obj' : obj,
            'form' :form
        }
    except Exception as e:
        print(e)
        raise Http404

    return render(request, "blogapp/update_blog.html", context)

@login_required
def delete_blog_post(request , id):
    try:
        obj = Blog.objects.get(pk = id)
        obj.delete()
        return redirect("/blogs/blogs-list/")

    except Exception as e:
        print (e)
        raise Http404