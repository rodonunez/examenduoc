#from django.conf.urls import url
from django.urls import path, include
from  . import views
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin


urlpatterns = [
   #path('base', views.base, name='base'),
   path('', views.home, name='home'),
   path('nosotros', views.nosotros, name='nosotros'),
   path('contacto', views.contacto, name='contacto'),
   path('galeria', views.galeria, name='galeria'),
   
   # CRUD
   path('gestiongal', views.gestiongal, name='gestiongal'),
   path('nuevogal', views.nuevogal, name='nuevogal'),  
   path('editargal/<codigo>', views.editargal, name='editargal'),
   path('borrargal/<codigo>', views.borrargaleria, name='borrargal'),   

   # GESTION USUARIOS
   path('login', views.login, name='login'),
   path('salir', views.salir, name='salir'),
      
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
