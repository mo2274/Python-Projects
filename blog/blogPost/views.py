from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import PostForm

def index(request):
    posts = BlogPost.objects.all().order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogPost/index.html', context)


def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogpost:index')
    context = {'form': form}
    return render(request, 'blogPost/new_post.html', context)


def post(request, id):
    post = BlogPost.objects.get(id=id)
    context = {'post': post}
    return render(request, 'blogPost/post.html', context)


def edit_post(request, id):
    post = BlogPost.objects.get(id=id)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogpost:post', id=id)
    context = {'post': post, 'form': form}
    return render(request, 'blogPost/edit_post.html', context)
        
def delete_post(request, id):
    post = BlogPost.objects.get(id=id)
    if post:
        post.delete()
    return redirect('blogpost:index')