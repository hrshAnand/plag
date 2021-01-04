from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from django.contrib import messages
import os


def IndexView(request):
    form = FileForm(request.POST, request.FILES)

    if request.method == "POST":
        if True:
            print("we r in")
            print(form)
            f1 = request.FILES['file1']
            f2 = request.FILES['file2']

            fs = FileSystemStorage()
            f1n = fs.save(f1.name, f1)
            f2n = fs.save(f2.name, f2)

            lans = {
                'c': 'c',
                'cpp': 'cc',
                'py': 'python',
                'cs': 'csharp',
                'js': 'javascript',
            }

            if f1n.split('.')[-1] != f2n.split('.')[-1]:
                return HttpResponse("Files of different languages!")

            ext = f2n.split('.')[-1]
            if ext not in lans:
                return HttpResponse(".{} files are not yet supported!\n You can only check plagiarism for the following files:{}".format(ext, lans.keys()))

            ls_fd = os.popen(
                "cd media;chmod 0755 mossnet.pl;./mossnet.pl -l {} {} {} ".format(lans[ext], f1n, f2n))
            output = ls_fd.read()
            print(output)
            ls_fd.close()
            ls_fd = os.popen("cd media;rm {};rm {}".format(f1n, f2n))
            ls_fd.close()
            output = str(output).split()
            return HttpResponseRedirect(output[0])

    return render(request, 'plagapp/index.html', {"form": FileForm()})
