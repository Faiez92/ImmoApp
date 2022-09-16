from django.contrib import admin

from ImmoApp.models.models import Appartement
from ImmoApp.models.program import Program

admin.site.register(Appartement)
admin.site.register(Program)