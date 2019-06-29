from django.shortcuts import render
from . import models 

def home(request):
	data = {
		'news' : models.Article.objects.all(),
		'title' : 'Главная страница',
	}
	return render(request, 'home/home.html', data)

def contacts(request):
	return render(request, 'home/contacts.html')