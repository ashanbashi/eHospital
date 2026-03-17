from django.contrib import admin
from eHospitalapp.models import *

# Register your models here.
admin.site.register(MyPatient)
admin.site.register(MyAppointment)
admin.site.register(Doctor)
admin.site.register(Transaction)