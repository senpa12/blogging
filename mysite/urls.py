from django.contrib import admin
from django.urls import path, include
################ Untuk Media ##############
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt



from mysite.views import *

from mysite.authentication import login, logout, registrasi

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),
    path('artikel/<int:id>', detail_artikel, name="detail_artikel"),
    path('artikel_not_found', not_found_artikel, name="not_found_artikel"),
    path('kontak', kontak, name='kontak'),
    path('galeri', galeri, name='galeri'),
    
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/artikel-list', artikel_list, name='artikel_list'),

    path("ckeditor5/", include('django_ckeditor_5.urls')),


    path('dashboard/', include("artikel.urls")),

    ############################# Auhtentication #########################

    path('auth-login', login, name='login'),
    path('auth-registrasi', registrasi, name='registrasi'),
    path('auth-logout', logout, name='logout'),
]


############################### untuk media #####################

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [
#     path("ckeditor5/", include('django_ckeditor_5.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)