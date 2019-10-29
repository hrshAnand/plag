from django.shortcuts import render
from plagapp.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import os, time
def index(request):
	return render(request,'plagapp/index.html')

@login_required
def upload_files(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        ls_fd = os.popen('cd media&&dir')
        output = ls_fd.read()+"WIN    "
        ls_fd.close()
        ls_fd = os.popen('cd media&&./mossnet.txt 1.c 1.c')
        time.sleep(10)
        output += ls_fd.read()+"UNIX"
        ls_fd.close()
        return HttpResponse(output)
        return render(request, 'plagapp/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request,'plagapp/upload.html')

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'plagapp/upload.html', {
        'form': form
    })

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_form.email = request.POST.get('email')
        user_form.username = request.POST.get('username')
        user_form.password = request.POST.get('password')
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return render(request,'plagapp/index.html')
        else:
            return HttpResponse(user_form.errors)

    else:
        user_form = UserForm()
        #profile_form = UserProfileInfoForm()
    return render(request,'plagapp/register.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('upload_files'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'plagapp/login.html', {})