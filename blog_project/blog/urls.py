from django.urls import path
from .views import BlogListView, BlogDetailView ,AboutView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
]