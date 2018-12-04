from django.shortcuts import render
from .models import Post

from django.http import HttpResponse

# posts = [
#     {
#         'author': 'AmberWu',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'November 29, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'November 25, 2018'
#     }

# ]


def home(request):
	return HttpResponse('<h1>!Secure Strolls DJANGO TEST!</h1>')
    # context = {
    #     'posts': posts
    # }

    # context = {
    #     'posts': Post.objects.all()
    # }

    # return render(request, 'blog/home.html', context)

# def about(reauest):
#     return HttpResponse('<h1>Blog About</h1>')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

