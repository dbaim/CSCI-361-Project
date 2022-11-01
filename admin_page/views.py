from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse


def admin_welcome(request):
    return render(request, 'admin_page/welcome_page.html')


def login(request):
    return render(request, 'admin_page/login_page.html')


def about(request):
    return HttpResponse("<h4>The hospital management system has a goal of providing a basic functionality for the patients and the hospital staff (doctors, nurses, managers, administration) to automate the processes of making an appointment, maintaining patient history, and prescribing medications and treatment procedures.</h4>")
