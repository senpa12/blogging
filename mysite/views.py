from django.shortcuts import render, redirect
from artikel.models import Kategori, ArtikelBlog

def index(request):
    template_name = "landingpage/index.html"
    kategori = Kategori.objects.all()
    artikel = ArtikelBlog.objects.all()
    print(artikel)

    context = {
        "title":"selamat datang",
        "kategori":kategori,
        "artikel":artikel
    }
    return render(request, template_name, context) 

def detail_artikel(request, id):
    template_name = "landingpage/detail.html"
    try:
        artikel = ArtikelBlog.objects.get(id=id)
    except ArtikelBlog.DoesNotExist:
        return redirect(not_found_artikel)

    artikel_lainnya = ArtikelBlog.objects.all().exclude(id=id)

    context = {
        "title":"selamat datang",
        "artikel":artikel,
        "artikel_lainnya":artikel_lainnya,
    }
    return render(request, template_name, context)

def not_found_artikel(request):
    template_name = "artikel_not_found.html"
    return render(request, template_name) 



def kontak(request):
    template_name = "kontak.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)

def galeri(request):
    template_name = "galeri.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)




def dashboard(request):
    if not request.user.is_authenticated:
        pesan = "anda belum login"
        return redirect('login')
    
    template_name = "dashboard/index.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)

def artikel_list(request):
    template_name = "dashboard/artikel_list.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)
