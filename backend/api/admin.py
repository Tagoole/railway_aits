from django.contrib import admin
from .models import CustomUser, Department,Issue,Course_unit

admin.site.register(CustomUser)
admin.site.register(Department)
admin.site.register(Issue)
admin.site.register(Course_unit)
