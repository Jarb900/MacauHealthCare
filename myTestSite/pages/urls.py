from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('/login',views.homePageView, name='login'),
    path('home/', views.homePageView, name='home2'),
    path('about/',views.AboutPageView.as_view(), name='about')
]