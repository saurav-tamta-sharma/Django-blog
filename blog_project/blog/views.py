from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post
from .forms import PostForm

# Home view to display all posts
def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/home.html', {'posts': posts})

# Create a new post view (requires login)
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('blog-home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('blog-home')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Post detail view to display a specific post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Fetches the post with the primary key of 5 in this case
    return render(request, 'blog/post_detail.html', {'post': post})
