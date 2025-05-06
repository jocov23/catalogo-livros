from django.contrib import admin
from django.urls import path, include

#primary URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('livros.urls')),
]
