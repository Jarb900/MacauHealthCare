from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Doctor, Patient, Appointment
from .forms import AppointmentForm

def home(request):
    appointments = Appointment.objects.all()
    paginator = Paginator(appointments, 10)  # Pagination
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'object_list': page_obj})

def doctor_list(request):
    doctors = Doctor.objects.all().order_by('user__last_name')
    return render(request, 'clinic/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, id, slug):
    doctor = get_object_or_404(Doctor, id=id, slug=slug)
    appointments = Appointment.objects.filter(doctor=doctor, status='a')

    if request.method == 'POST' and request.user.is_authenticated:
        if hasattr(request.user, 'patient'):
            patient = Patient.objects.get(user=request.user)
            selected_appoint_id = request.POST.get('appointment')
            if selected_appoint_id:
                appointment = Appointment.objects.get(pk=selected_appoint_id)
                appointment.patient = patient
                appointment.status = 't'
                appointment.save()
                return redirect('my_appointment')

    context = {
        'doctor': doctor,
        'appointments': appointments,
    }
    return render(request, 'clinic/doctor_detail.html', context)

def is_doctor(user):
    return user.groups.filter(name='ClinicStaff').exists()

@login_required
@user_passes_test(is_doctor, login_url='/login/', redirect_field_name=None)
def patient_list(request):
    patients = Patient.objects.all().order_by('user__last_name')
    return render(request, 'clinic/patient_list.html', {'patients': patients})

@login_required
@user_passes_test(is_doctor, login_url='/login/', redirect_field_name=None)
def patient_detail(request, id):
    patient = get_object_or_404(Patient, id=id)
    appointments = Appointment.objects.filter(patient=patient, status='t')
    return render(request, 'clinic/patient_detail.html', {'patient': patient, 'appointments': appointments})

class AvailableAppointmentsView(ListView):
    model = Appointment
    template_name = "clinic/available_appointments.html"

    def get_queryset(self):
        return Appointment.objects.filter(status="a")

class AvailableAppointmentsView2(ListView):
    model = Appointment
    template_name = "clinic/home.html"
    context_object_name = 'object_list'
    paginate_by = 2

    def get_queryset(self):
        return Appointment.objects.filter(status="a")

@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":
        appointment_id = request.POST.get('appointment_id')
        appointment = get_object_or_404(Appointment, id=appointment_id, doctor=doctor, status='available')

        appointment.patient = request.user.patient
        appointment.status = 't'
        appointment.save()

        return HttpResponseRedirect(reverse('my_appointment'))

    available_appointments = Appointment.objects.filter(doctor=doctor, status='available')
    return render(request, 'doctor_detail.html', {
        'doctor': doctor,
        'appointments': available_appointments
    })

@login_required
@user_passes_test(is_doctor, login_url='/login/', redirect_field_name=None)
def add_appointment(request):
    doctor = Doctor.objects.get(user=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.status = 't'
            appointment.save()
            return redirect('my_appointment')
    else:
        form = AppointmentForm()

    return render(request, 'add_appointment.html', {'form': form})

@login_required
def my_appointment(request):
    if hasattr(request.user, 'patient'):
        patient = Patient.objects.get(user=request.user)
        appointments = Appointment.objects.filter(patient=patient, status='t')
    elif hasattr(request.user, 'doctor'):
        doctor = Doctor.objects.get(user=request.user)
        appointments = Appointment.objects.filter(doctor=doctor, status='t')
    else:
        appointments = []

    return render(request, 'clinic/my_appointment.html', {'appointments': appointments})