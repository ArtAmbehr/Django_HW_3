"""
Some Infos
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views as views_myapp

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views_myapp.hello_world),  # Таким образом вывел для себя
    path("myapp/", include('myapp.urls')),
]
