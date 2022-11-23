from django.shortcuts import render
from djangoapp.models import doctModel
from djangoapp.models import PatientModel
from djangoapp.models import AppointmentModel
from django.contrib import messages
from djangoapp.forms import doctForms
from djangoapp.forms import PatientForms
from djangoapp.forms import AppointmentForms
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.http import HttpResponse


def showDoct(request) :
    showDoct = doctModel.objects.all()
    showPat = PatientModel.objects.all()
    return render(request, 'index.html', {"data":showDoct, "dataPat": showPat})


def insertion(request) :
    if request.method == "POST" :
        if request.POST.get('dateofbirth') and request.POST.get('iin') and request.POST.get('doctorid') and request.POST.get('patientid') and request.POST.get('username') and request.POST.get('fullname') and request.POST.get('phonenumber') and request.POST.get('departmentid') and request.POST.get('specializationsid') and request.POST.get('experience') and request.POST.get('category') and request.POST.get('price') and request.POST.get('scheduledetails') and request.POST.get('education') and request.POST.get('rating') and request.POST.get('address') and request.POST.get('email') :
            saverecord = doctModel()
            saverecord.dateofbirth = request.POST.get('dateofbirth') 
            saverecord.iin = request.POST.get('iin')
            saverecord.doctorid = request.POST.get('doctorid')
            saverecord.patientid = request.POST.get('patientid')
            saverecord.username = request.POST.get('username')
            saverecord.fullname = request.POST.get('fullname')
            saverecord.phonenumber = request.POST.get('phonenumber')
            saverecord.departmentid = request.POST.get('departmentid')
            saverecord.specializationsid = request.POST.get('specializationsid')
            saverecord.experience = request.POST.get('experience')
            saverecord.category = request.POST.get('category')
            saverecord.price = request.POST.get('price')
            saverecord.scheduledetails = request.POST.get('scheduledetails')
            saverecord.education = request.POST.get('education')
            saverecord.rating = request.POST.get('rating')
            saverecord.address = request.POST.get('address')
            saverecord.email = request.POST.get('email')
            saverecord.save()
            messages.success(request,'Saved successfully!')
            return render(request, 'Insert.html')
    else :
            return render(request, 'Insert.html')


def insertionPat(request) :
    if request.method == "POST" :
        if request.POST.get('dob') and request.POST.get('iin') and request.POST.get('patientid') and request.POST.get('full_name') and request.POST.get('blood_group') and request.POST.get('emergency_contact_number') and request.POST.get('contact_number') and request.POST.get('email') and request.POST.get('home_address') and request.POST.get('marital_status') and request.POST.get('registration_date') and request.POST.get('username') and request.POST.get('doctorid')  :
            saverecord = PatientModel()
            saverecord.dob = request.POST.get('dob') 
            saverecord.iin = request.POST.get('iin')
            saverecord.patientid = request.POST.get('patientid')
            saverecord.full_name = request.POST.get('full_name')
            saverecord.blood_group = request.POST.get('blood_group')
            saverecord.emergency_contact_number = request.POST.get('emergency_contact_number')
            saverecord.contact_number = request.POST.get('contact_number')
            saverecord.email = request.POST.get('email')
            saverecord.home_address = request.POST.get('home_address')
            saverecord.marital_status = request.POST.get('marital_status')
            saverecord.registration_date = request.POST.get('registration_date')
            saverecord.username = request.POST.get('username')
            saverecord.doctorid = request.POST.get('doctorid')
            saverecord.save()
            messages.success(request,'Saved successfully!')
            return render(request, 'InsertPat.html')
    else :
            return render(request, 'InsertPat.html')


def update(request, id) :
    editobject = doctModel.objects.get(doctorid = id)
    return render(request, 'edit.html', {"doctModel":editobject})


def updateTable(request, id) :
    UpdateTable=doctModel.objects.get(doctorid = id)
    form=doctForms(request.POST,instance=UpdateTable)
    if form.is_valid :
        form.save()
        messages.success(request,'Updated successfully')
        return render(request, 'edit.html', {"doctModel":UpdateTable})


def deleteRecord(request, id) :
    deleterecord=doctModel.objects.get(doctorid = id)
    deleterecord.delete()
    showdata = doctModel.objects.all()
    showPat = PatientModel.objects.all()
    return render(request, "delete.html", {"data":showdata, "dataPat":showPat})
    

def deletePatRecord(request, id) :
    deleterecord=PatientModel.objects.get(patientid = id)
    deleterecord.delete()
    showPat = PatientModel.objects.all()
    showdata = doctModel.objects.all()
    return render(request, "delete.html", {"dataPat":showPat, "data":showdata})


def updatePat(request, id) :
    editobject = PatientModel.objects.get(patientid = id)
    return render(request, 'editPat.html', {"PatientModel":editobject})


def updateTablePat(request, id) :
    UpdateTablePat=PatientModel.objects.get(patientid = id)
    form=PatientForms(request.POST,instance=UpdateTablePat)
    if form.is_valid :
        form.save()
        messages.success(request,'Updated successfully')
        return render(request, 'editPat.html', {"PatientModel":UpdateTablePat})


def login(request):
    showDoct = doctModel.objects.all()
    showPat = PatientModel.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                auth.login(request, user)
                return render(request, 'index.html', {"data":showDoct, "dataPat": showPat})
            else:
                messages.error(request, "U R not an admin!!!")
                return redirect('/')
        else:
            if not User.objects.filter(username=username).exists():
                messages.error(request, "Username Doesn't Exist")
            else:
                messages.info(request, "Incorrect Password")
            return redirect('/')

    else:  
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def welcome(request):
    return render(request, 'welcome_page.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def patient_appointment(request):
    return render(request, 'patient_appointment.html')


def home_page(request):
    return render(request, 'home_page.html')


def appointment_check(request, date):
    UpdateTable = AppointmentModel.objects.get(date=date)
    form = AppointmentForms(request.POST, instance=UpdateTable)
    if form.is_valid():
        form.save()
        messages.success(request, 'Updated successfully')
        return render(request, 'welcome_page.html', {"users": UpdateTable})


