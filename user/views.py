from django.shortcuts import render, redirect
from .forms import PostForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post
import datetime
from django.http import HttpResponse

def login_page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'user/login.html', context)


def register_page(request):
    user_form = CreateUserForm()
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')

    context = {
        'form': user_form
    }

    return render(request, 'user/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home_page(request):
    user_posts = Post.objects.filter(user=request.user)
    context = {
        'posts': user_posts
    }
    return render(request, 'user/home.html', context)


@login_required(login_url='login')
def add_post(request):
    print(request.user)
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            print("Entered Here")
            new_post_form = post_form.save(commit=False)
            new_post_form.user = request.user
            new_post_form.updated_at = datetime.datetime.now()
            new_post_form.save()
            return redirect('home')

    else:
        post_form = PostForm()

    context = {
        'form': post_form
    }
    return render(request, 'user/add_post.html', context)


def edit_post(request, id):
    curr_post = Post.objects.get(id=id)
    formset = PostForm(instance=curr_post)
    if request.method == 'POST':
        formset = PostForm(request.POST, instance=curr_post)
        if formset.is_valid():
            new_formset = formset.save(commit=False)
            new_formset.updated_at = datetime.datetime.now()
            new_formset.save()
            return redirect('home')
    context = {'form': formset}
    return render(request, 'user/edit_post.html', context)


def delete_post(request, id):
    curr_post = Post.objects.get(id=id)
    curr_post.delete()
    return redirect('home')
