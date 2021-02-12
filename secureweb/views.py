from django.shortcuts import render, redirect
from secureweb.models import Web
from secureweb.forms import FormWeb
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil nyieun akun")
            return redirect('signup')
        else:
             messages.error(request, "Hubungi pembuat")
             return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form
        }
    return render(request, 'signup.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_project(request, id_project):
    project = Web.objects.filter(id=id_project)
    project.delete()

    messages.success(request, "belegug sia mah ngadon di hapus emang infona geus ngarubah? mun enggeus mah bae")
    return redirect('project')

@login_required(login_url=settings.LOGIN_URL)
def ubah_project(request, id_project):
    project = Web.objects.get(id=id_project)
    template = 'ubah-project.html'
    if request.POST:
        form = FormWeb(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "web data updated successfully")
            return redirect('ubah_project', id_project=id_project)
    else:
        form = FormWeb(instance=project)
        konteks = {
            'form':form,
            'project':project,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def project(request):
  
    proyek = Web.objects.all()


    konteks = {
        'proyek': proyek,
    }
    return render(request, 'project.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def pembuat(request):
    return render(request, 'pembuat.html')

@login_required(login_url=settings.LOGIN_URL)
def tambah_web(request):
    if request.POST:
        form = FormWeb(request.POST)
        if form.is_valid():
            form.save()
            form = FormWeb()
            pesan = "Daftar Web Berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-web.html', konteks)
    else:
        form = FormWeb()

        konteks = {
            'form': form,
        }
    return render(request, 'tambah-web.html', konteks)