from django.shortcuts import render
from . import forms

def landing(request):
	name = 'Alex'
	form = forms.CustomerForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		print(form.cleaned_data)
		save_form = form.save()
	return render(request, 'landing/landing.html', locals())