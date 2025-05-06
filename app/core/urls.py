from django.contrib import admin
from django.urls import path, include

#primary URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('livros.urls')), #html interface
    #path('api/', include('livros.urls')), #api interface
]
