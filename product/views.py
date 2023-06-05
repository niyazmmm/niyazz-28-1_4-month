from django.shortcuts import render
from django.http import HttpResponse
import datetime

def helloworld(request):
    if request.method == 'GET':
        return HttpResponse('Hello world')

def goodbye(request):
    if request.method == 'GET':
        return HttpResponse('Good bye')

def nowdate(request):
    if request.method == 'GET':
        datetim = datetime.datetime.now()
        return HttpResponse(datetim)

    return render (request, 'users/register.html'), content
from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Hashtag, Comment
from posts.forms import PostCreateForm, CommentCreateForm, HashtagCraeteForm

from users.utils import get_user_from_request

# Create your views here.
def posts_view(request):
@@ -12,15 +12,17 @@ def posts_view(request):
        else:
            posts = Post.objects.all()
        context = {
            'posts': posts
            'posts': posts,
            'user': get_user_from_request(request)
        }
        return render(request, 'posts/posts.html', context=context)


def hashtags_view(request, **kwargs):
    if request.method == 'GET':
        context = {
            'hashtags': Hashtag.objects.all()
            'hashtags': Hashtag.objects.all(),
            'user': get_user_from_request(request)
        }
        return render(request, 'posts/hashtags.html', context=context)

@@ -32,7 +34,8 @@ def detail_view(request, **kwargs):
        data = {
            'post': post,
            'comments': Comment.objects.filter(id=kwargs['id']),
            'form': CommentCreateForm
            'form': CommentCreateForm,
            'user': get_user_from_request(request)
        }
        return render(request, 'posts/detail.html', context=data)

@@ -48,7 +51,8 @@ def detail_view(request, **kwargs):
            data = {
                'post': post,
                'comments': Comment.objects.filter(post_id=kwargs['id']),
                'form': CommentCreateForm
                'form': CommentCreateForm,
                'user': get_user_from_request(request)
            }
            return render(request, 'posts/detail.html', context=data)

@@ -58,15 +62,17 @@ def detail_view(request, **kwargs):
            data = {
                'post': post,
                'comments': comment,
                'form': CommentCreateForm
                'form': CommentCreateForm,
                'user': get_user_from_request(request)
            }
            return render(request, 'posts/detail.html', context=data)


def posts_create_view(request):
    if request.method == 'GET':
        data = {
            'form': PostCreateForm
            'form': PostCreateForm,
            'user': get_user_from_request(request)
        }
        return render(request, 'posts/create_post.html', context=data)
    if request.method == 'POST':
@@ -82,26 +88,30 @@ def posts_create_view(request):
            return redirect('/posts')
        else:
            data = {
                'form': form
                'form': form,
                'user': get_user_from_request(request)

            }
            return render(request, 'posts/create_post.html', context=data)


from django.shortcuts import render, HttpResponse, redirect
from users.forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from users.utils import get_user_from_request
from django.contrib.auth.models import User


# Create your views here.
def login_view(request):
    if request.method == 'GET':
        data = {
            'form': LoginForm,
            'user': get_user_from_request(request)

        }
        return render(request, 'users/login.html', context=data)
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/posts')
            else:
                form.add_error("username", "Bad request")
        data = {
            "form": form
        }
        return render(request, 'users/login.html', context=data)


def logout_view(request):
    logout(request)
    return redirect('/posts/')


def register_view(request):
    if request.method == 'GET':
        data = {
            'form': RegisterForm,
            'user': get_user_from_request(request)
        }
        return render(request, 'users/register.html', context=data)
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                login(request, user)
                return redirect('/posts')
            else:
                form.add_error('password1', 'Password do not match')
        data = {
            'form': form,
            'user': get_user_from_request(request)
        }
        return render(request, 'users/register.html', context=data)


    def posts_view(request):
        if request.method = 'GET':
            posts = Post.objects.all()
            search = request.GET.get('search')

            max_page = posts.__len__() / PAGINATION_LIMIT









