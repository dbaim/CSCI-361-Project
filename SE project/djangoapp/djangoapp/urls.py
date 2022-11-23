from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_page', views.showDoct, name="showDoct"),
    path('about', views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('Insert', views.insertion, name="insertion"),
    path('edit/<int:id>', views.update, name="update"),
    path('update/<int:id>', views.updateTable, name="updateTable"),
    path('delete/<int:id>', views.deleteRecord, name="deleteRecord"),
    path('', views.welcome, name="welcome"),
    path('InsertPat', views.insertionPat, name="insertionPat"),
    path('deletePat/<int:id>', views.deletePatRecord, name="deletePatRecord"),
    path('editPat/<int:id>', views.updatePat, name="updatePat"),
    path('updatePat/<int:id>', views.updateTablePat, name="updateTablePat"),
    path('login', views.login, name="login"),
    path('home', views.home_page, name='home'),
    path('appointment_page', views.patient_appointment, name='appointment')
]
