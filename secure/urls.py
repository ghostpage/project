from django.contrib import admin
from django.urls import path
from secureweb.views import *
from django.contrib.auth.views import LoginView, LogoutView
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', project, name='project'),
    path('pembuat/', pembuat, name='pembuat'),
    path('tambah-web/', tambah_web, name='tambah_web'),
    path('project/ubah/<int:id_project>', ubah_project, name='ubah_project'),   
    path('project/hapus/<int:id_project>', hapus_project, name='hapus_project'), 
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('signup/', signup, name='signup'),
]