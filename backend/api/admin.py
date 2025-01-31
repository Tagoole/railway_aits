from django.contrib import admin
from .models import CustomUser, Department,Issue,Audit_Trail

admin.site.register(CustomUser)
admin.site.register(Department)
admin.site.register(Issue)
admin.site.register(Audit_Trail)