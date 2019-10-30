from django.shortcuts import render
from plagapp.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import os, time, subprocess 
def index(request):
	return render(request,'plagapp/index.html')

@login_required
def upload_files(request):
    if request.method == 'POST' and request.FILES['f1'] and request.FILES['f2']:
        f1 = request.FILES['f1']
        f2 = request.FILES['f2']
        fs = FileSystemStorage()
        file1 = fs.save("base.c", f1)
        file2 = fs.save("source.c", f2)
        #uploaded_file_url = fs.url(file1)
        ls_fd = os.popen("cd media;chmod 0755 mossnet.pl;./mossnet.pl base.c source.c")
        output = ls_fd.read()
        print(output)
        ls_fd.close()
        ls_fd = os.popen("cd media;rm base.c;rm source.c")
        ls_fd.close()
        output=str(output).split()
        #return HttpResponseRedirect("https://google.com")
        return HttpResponseRedirect(output[0]+"match0.html")
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