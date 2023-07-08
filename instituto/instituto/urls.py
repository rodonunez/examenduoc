from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('artistas.urls')),
    
    
    path("accounts/", include("django.contrib.auth.urls")),

]

print("paso por urls de grupo cero")