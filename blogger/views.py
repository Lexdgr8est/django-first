from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def home(request):
	#return HttpResponse('Hello from rootlexh')

	posts = Post.objects.all()[:10]

	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)


def post(request):
	return render(request, 'blog/post.html')


def contact(request):
	return render(request, 'blog/contact.html')

def about(request):
	return render(request, 'blog/about.html')