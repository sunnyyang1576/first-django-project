from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,Author
from .forms import BlogForm

# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()
    authors = Author.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs, 'authors': authors})


def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form': form})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    blogs = author.blog_set.all()
    return render(request, 'author_detail.html', {'author': author, 'blogs': blogs})