from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import PostForm

def check_post_owener(request, post):
    if request.user != post.user:
        raise Http404


def post_view(posts):
    for post in posts:
        if len(post.text) > 50:
            post.text = post.text[:50] + '...'


def index(request):
    return render(request, 'blogPost/index.html')


@login_required
def posts(request):
    posts = BlogPost.objects.filter(user=request.user).order_by('date_added')
    post_view(posts)
    context = {'posts': posts}
    return render(request, 'blogPost/posts.html', context)


@login_required
def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('blogpost:posts')
    context = {'form': form}
    return render(request, 'blogPost/new_post.html', context)


@login_required
def post(request, id):
    post = BlogPost.objects.get(id=id)
    check_post_owener(request, post)
    context = {'post': post}
    return render(request, 'blogPost/post.html', context)


@login_required
def edit_post(request, id):
    post = BlogPost.objects.get(id=id)
    check_post_owener(request, post)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogpost:post', id=id)
    context = {'post': post, 'form': form}
    return render(request, 'blogPost/edit_post.html', context)


@login_required       
def delete_post(request, id):
    post = BlogPost.objects.get(id=id)
    check_post_owener(request, post)
    if post:
        post.delete()
    return redirect('blogpost:posts')