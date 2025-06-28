from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login (request):
    template_name = "login.html"
    pesan = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            pesan = "username dan password wajib diisi"
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                pesan = "berhasil login"
                return redirect('/')
            else:
                pesan = "username atau password salah"

    context = {
        'pesan':pesan
    }
    return render (request, template_name, context)
    
def registrasi(request):
    template_name = "registrasi.html"
    pesan = ''

    if request.method == "POST":
        username = request.POST.get('username')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validasi input kosong
        if not username or not nama_depan or not nama_belakang or not password1 or not password2:
            pesan = "Semua data wajib diisi yah"
        elif password1 != password2:
            pesan = "Password 1 dan 2 tidak sama"
        elif User.objects.filter(username=username).exists():
            pesan = "Username sudah digunakan"
        else:
            # Buat user baru dan langsung set password-nya
            user = User.objects.create_user(
                username=username,
                first_name=nama_depan,
                last_name=nama_belakang,
                password=password1
            )
            return redirect('/')  # Atau redirect ke login

    context = {
        'pesan': pesan
    }
    return render(request, template_name, context)

def logout(request):
    auth_logout(request)
    return redirect('/')