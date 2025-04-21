from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('clinic.urls')),
    path("clinic/", include("clinic.urls")),
    path("accounts/", include ('django.contrib.auth.urls')),
]
