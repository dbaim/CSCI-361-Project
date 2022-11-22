from django.db import models
from datetime import datetime, date


class doctModel(models.Model) :
    dateofbirth = models.DateField(auto_now_add = False, auto_now = False, blank = False)
    iin = models.CharField(max_length = 12)
    doctorid = models.IntegerField(primary_key = True)
    patientid = models.IntegerField()
    username = models.CharField(max_length = 50)
    fullname = models.CharField(max_length = 255)
    phonenumber = models.CharField(max_length = 12)
    departmentid = models.IntegerField()
    specializationsid = models.IntegerField()
    experience = models.IntegerField()
    category = models.CharField(max_length = 50)
    price = models.IntegerField()
    scheduledetails = models.CharField(max_length = 255)
    education = models.CharField(max_length = 50)
    rating = models.IntegerField()
    address = models.CharField(max_length = 50)
    email = models.CharField(max_length = 250)

    class Meta:
        db_table = "doctor"


class PatientModel(models.Model):
    dob = models.DateField(auto_now_add = False, auto_now = False, blank = False)
    iin = models.CharField(max_length = 12)
    patientid = models.IntegerField(primary_key = True)
    full_name = models.CharField(max_length = 255)
    blood_group = models.CharField(max_length = 50)
    emergency_contact_number = models.CharField(max_length = 12)
    contact_number = models.CharField(max_length = 12)
    email = models.CharField(max_length = 250)
    home_address = models.CharField(max_length = 250)
    marital_status = models.CharField(max_length = 250)
    registration_date = models.DateField(auto_now_add = False, auto_now = False, blank = False)
    username = models.CharField(max_length = 50)
    doctorid= models.IntegerField()

    class Meta:
        db_table = "patients"


class AppointmentModel(models.Model):
    app_id = models.IntegerField()
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(unique=True)
    doctor = models.ForeignKey(doctModel, db_column='doctorid', on_delete=models.CASCADE)
    patient = models.OneToOneField(PatientModel, db_column='patientid', on_delete=models.CASCADE)
    available = models.BooleanField()

    class Meta:
        db_table = "appointment"
        constraints = [
            models.UniqueConstraint(fields=['date', 'doctor'], name='appointment')
        ]
