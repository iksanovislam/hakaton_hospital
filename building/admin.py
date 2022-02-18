from django.contrib import admin
from .models import Hospital, GlavVrach, Medsestra, Terapevt, Hirurg, Patients

admin.site.register(Hospital)
admin.site.register(GlavVrach)
admin.site.register(Medsestra)
admin.site.register(Terapevt)
admin.site.register(Hirurg)
admin.site.register(Patients)
