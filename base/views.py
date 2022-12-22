from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import logging
logger = logging.getLogger(__name__)
# Create your views here.

def loginreq(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'base/login.html', context)

def register(request):
    if request.method != 'POST':
        return render(request, 'base/register.html')
    # Check if user exists
    username = request.POST['uname']
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    email = request.POST['email']
    password = request.POST['pass']
    user_exist = False
    try:
        User.objects.get(username=username)
        user_exist = True
    except:
        logger.error("New user")
    if not user_exist:
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,email=email,
                                        password=password)
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, 'User already exists')
        return render(request, 'base/register.html')

def logout_req(request):
    logout(request)
    return render(request, 'base/form.html')


def home(request):
    if request.method == "POST":
        files = request.FILES['file']
        doc = Document.objects.create(file=files, user=request.user)
        doc.save()
        messages.success(request, 'File was uploaded successfully')
        return redirect('home')
    return render(request, 'base/form.html')

def files(request):
    user = request.user
    docs = user.document_set.all()
    context = {'docs': docs}
    return render(request, 'base/files.html', context)