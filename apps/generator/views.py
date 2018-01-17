from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):


	if 'counter' not in request.session:
		request.session['counter'] = 0
		return render(request, 'generator/index.html')

	else:
		request.session['counter'] += 1
	
		return render(request,'generator/index.html')

def create(request):
	if request.method == 'POST':
		request.session['unique'] = get_random_string(length = 32)

	return redirect('/')

def reset(request):
	if request.method == 'POST':
		del request.session['counter']
		del request.session['unique']


	return redirect('/')

# Create your views here.
