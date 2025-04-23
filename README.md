# Macau Health Care

## 🖼️ Graphical Abstract
> <img src="https://github.com/user-attachments/assets/d589e297-c095-474f-9efd-7e014e8579db" width="700">
<blockquote class="imgur-embed-pub" lang="en" data-id="a/GVMikfx"  ><a href="//imgur.com/a/GVMikfx">Booking System</a></blockquote> 
*A visual summary of how users interact with the system: Patients → Book → Doctors → Add availability*

## 📹 Demo

[Demo Video](https://youtu.be/7PM9Q8Fbbcs)

## 💻 Development Environment

| Component   | Details                    |
|-------------|----------------------------|
| Language    | Python 3.10                |
| Framework   | Django 4.2                 |
| DB          | SQLite (default Django DB) |
| Platform    | pythonanywhere.com         |


---

## 🎯 Purpose of the Software

This project is a simple yet functional **Appointment Booking System** designed to allow patients to book available appointment slots with doctors.

### 🔄 Software Development Model: **Agile**
We chose Agile because:
- It supports **iterative development**
- Allows **flexible task management** among group members
- We could adapt features quickly as the system evolved

### 👥 Target Users
- **Patients** who want to book appointments
- **Doctors** who provide appointment slots
- Optional: **Admins** for basic user/slot management

---

## 🛠 Software Development Plan

### 📌 Development Process
We followed an Agile model with:
- Weekly goals
- Regular check-ins
- Incremental feature builds

### 👤 Team Members

| Name        | Role            | Responsibilities                      | Contribution (%) |
|-------------|-----------------|----------------------------------------|------------------|
| P2426595    | Backend Developer | Models, Views, Appointment Logic       | 25%              |
| P2426616    | Frontend Developer | HTML Templates, CSS, UI Design         | 25%              |
| P2304171    | QA & Integration | Route Testing, Booking Flow, Bug Fixes | 25%              |
| P2426603   | Documentation & Video | README, Graphical Abstract, Demo Video | 25%              |

### 🗓 Development Schedule

| Week | Tasks Completed                          |
|------|-------------------------------------------|
| 1    | Setup Django project, user model          |
| 2    | Appointment models, user roles (Doctor/Patient) |
| 3    | Booking logic, UI templates               |
| 4    | README, demo video, deployment            |

---

## 🚧 Current Status
Login & Registration ✅

Doctor creates slots ✅

Patient books slots ✅

Data saved to DB ✅

## 🚀 Future Plan
Add notifications via email

Admin dashboard for user/slot overview

Calendar-based interface

Patient and Doctor details

---

### ⚙️ Algorithm (Simplified)

```python
# Home page shows all appointments with pagination
def home():
    appointments = get_all_appointments_paginated()

# Doctors are listed alphabetically
def list_doctors():
    return get_all_doctors_ordered()

# Show available appointments for selected doctor
def show_doctor_detail(doctor_id):
    if user_is_patient and request_is_post:
        appointment = get_selected_appointment()
        appointment.assign_to_patient(user)
        appointment.mark_as_taken()
        appointment.save()

# Access control: Only staff (doctors) can view patients
def can_access_patient_list(user):
    return user.in_group("ClinicStaff")

# View patient details with their appointments
def view_patient_detail(patient_id):
    if user_is_doctor:
        return get_patient_appointments(patient_id)

# Doctors can add new available appointments
def add_appointment():
    if user_is_doctor and form_is_valid:
        appointment.doctor = current_user
        appointment.status = 'available'
        appointment.save()

# Patients can book appointments if available
def book_appointment(doctor_id):
    if user_is_patient and appointment_is_available:
        appointment.assign_to_patient(user)
        appointment.status = 'taken'
        appointment.save()

# Authenticated users can view their own appointments
def my_appointment():
    if user_is_patient:
        return get_appointments_for_patient()
    elif user_is_doctor:
        return get_appointments_for_doctor()
