from django.contrib import admin

# Register your models here.
from .models import ProjectStatus, PropertyType, ServiceType, ObjectType, PaymentType, MainContractors, ClientType
# Register your models here.

admin.site.register(ProjectStatus)
admin.site.register(PropertyType)
admin.site.register(ServiceType)
admin.site.register(ObjectType)
admin.site.register(PaymentType)
admin.site.register(MainContractors)
admin.site.register(ClientType)