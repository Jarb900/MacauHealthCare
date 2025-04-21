from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('pages/', include('pages.urls')),
    path('', include('catalog.urls')),
    path('catalog/', include('catalog.urls')),
    ]