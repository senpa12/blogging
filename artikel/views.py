from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from artikel.models import Kategori
from artikel.models import ArtikelBlog
from artikel.forms import KategoriForm, ArtikelForms
from django.shortcuts import get_object_or_404
from .forms import UserEditForm
from django.contrib.auth.models import Group

# Create your views here.
def in_operator(user):
    get_user = user.groups.filter(name='Operator').count()
    if get_user == 0:
        return False
    else:
        return True


############################ User Biasa ################################
@login_required(login_url='/auth-login')
def artikel_list(request):
    template_name = "dashboard/pengguna/artikel_list.html"
    artikel = ArtikelBlog.objects.filter(created_by=request.user)
    context = {
        "artikel":artikel,
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil tambah artikel')
        return redirect(artikel_list)
    forms = ArtikelForms()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_update(request, id_artikel):
    template_name = "dashboard/admin/example.forms.html"
    try:
        artikel = ArtikelBlog.objects.get(id=id_artikel, created_by=request.user)
    except:
        messages.warning(request, "halaman yang diminta tidak ditemukan")
        return redirect("/dasboard")

    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil melakukan update artikel')
        return redirect(artikel_list)
    
    forms = ArtikelForms(instance=artikel)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_delete(request, id_artikel):
    try:
        Kategori.objects.get(id=id_artikel, created_by=request.user).delete()
        messages.success(request, 'berhasil delete artikel')
    except:
        messages.error(request, 'gagal delet artikel')
    
    return redirect(admin_artikel_list)






################ admin ######################
@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_list(request):
    template_name ="dashboard/admin/kategori_list.html"
    kategori = Kategori.objects.all()
    context = {
        "kategori":kategori
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_tambah(request):
    template_name = "dashboard/admin/kategori_forms.html"
    if request.method == "POST":
        forms = KategoriForm(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil tambah kategori')
        return redirect(admin_kategori_list)
    
    forms = KategoriForm()
    context = {
        "forms":forms
    }
    return render(request, 'dashboard/admin/kategori_forms.html', context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_update(request, id_kategori):
    template_name = "dasboard/admin/kategori_forms.html"
    kategori = Kategori.objects.get(id=id_kategori) 
    
    if request.method == "POST":
        forms = KategoriForm(request.POST, instance=kategori)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil update kategori')
        return redirect(admin_kategori_list)
    
    forms = KategoriForm(instance=kategori)
    context = {
        "forms":forms
    }
    return render(request, 'dashboard/admin/kategori_forms.html', context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_delete(request, id_kategori):
    try:
        Kategori.objects.get(id=id_kategori).delete()
        messages.success(request, 'berhasil delete kategori')
    except:
        messages.error(request, 'berhasil delete kategori')
    
    return redirect(admin_kategori_list)

##################################### Artikel blog #########################################

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_list(request):
    template_name ="dashboard/admin/artikel_list.html"
    artikel = ArtikelBlog.objects.all()
    context = {
        "artikel":artikel
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil tambah artikel')
        return redirect(admin_artikel_list)
    forms = ArtikelForms()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"
    artikel = ArtikelBlog.objects.get(id=id_artikel)
    
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil melakukan update artikel')
        return redirect(admin_artikel_list)
    
    forms = ArtikelForms(instance=artikel)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

# @login_required(login_url='/auth-login')
# @user_passes_test(in_operator, login_url='/')
# def admin_artikel_delete(request, id_artikel):
#     try:
#         ArtikelBlog.objects.get(id=id_artikel).delete()
#         messages.success(request, 'berhasil delete kategori')
#     except:
#         messages.error(request, 'berhasil delete kategori')
    
#     return redirect(admin_artikel_list)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_delete(request, id_artikel):
    try:
        ArtikelBlog.objects.get(id=id_artikel).delete()
    except:
        pass
    
    return redirect(admin_artikel_list)


##################################### Management User Oleh Operator ##########################################

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_list(request):
    template_name = "dashboard/admin/user_list.html"
    daftar_user = User.objects.all()
    context = {
        "daftar_user":daftar_user
    } 
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_edit(request, user_id):
    template_name = 'dashboard/admin/user_edit.html'
    user = get_object_or_404(User, pk=user_id)
    group_user = []
    for group in user.groups.all():
        group_user.append(group.name)

    all_groups = Group.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        is_staff = request.POST.get("is_staff")
        groups_checked = request.POST.getlist('groups')

        if is_staff == None:
            is_staff = False
        else:
            is_staff = True
        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = is_staff
        user.groups.set(Group.objects.filter(id_in=groups_checked))
        user.save()

        messages.success(request, f"berhasil update user {user.username}")
        return redirect(admin_management_user_list)

    context = {
        'user': user,
        'all_groups': all_groups,
        'group_user': group_user,
    }
    return render(request, template_name, context)