from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views
from .views import AvailableAppointmentsView, AvailableAppointmentsView2

urlpatterns = [
    path('', AvailableAppointmentsView2.as_view(), name='home'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:id>-<slug:slug>/', views.doctor_detail, name='doctor_detail'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:id>/', views.patient_detail, name='patient_detail'),
    path("appointments/available/", AvailableAppointmentsView.as_view(), name="available_appointments"),
    path('appointment/book/<int:appointment_id>/', views.book_appointment, name='book_appointment'),
    path('accounts/profile/', auth_views.LoginView.as_view(success_url=reverse_lazy('home')), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('newappoint/', views.add_appointment, name='add_appointment'),
    path('myappoint/', views.my_appointment, name='my_appointment'),
]
