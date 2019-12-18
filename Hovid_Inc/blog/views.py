from django.shortcuts import render
from .models import Post

posts = [
	{
		'author': 'J.K Rowling',
		'title': 'Harry Potter',
		'content': 'Wingardium Leviosa',
		'date_posted': 'November 26, 2019',

	},
	{
		'author': 'Mark Zuckerberg',
		'title': 'Facebook',
		'content': 'Social Life',
		'date_posted': 'December 01, 2019',

	}
]

def home(request):
	context = {
		'posts': Post.objects.all()

	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})