from django.contrib import admin

# Register your models here.
from .models import Carrera
from .models import Paralelo
from .models import Estudiante

admin.site.register(Carrera)
admin.site.register(Paralelo)
admin.site.register(Estudiante)
