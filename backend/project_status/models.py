from django.db import models

# Create your models here.
class ProjectStatus(models.Model):
    status = models.CharField(max_length=50, verbose_name="Статус")

    def __str__(self):
        return self.status

class PropertyType(models.Model):
    property_type = models.CharField(max_length=50, verbose_name="Тип собственности")

    def __str__(self):
        return self.property_type

class ServiceType(models.Model):
    service_type = models.CharField(max_length=50, verbose_name="Тип услуг")

    def __str__(self):
        return self.service_type

class ObjectType(models.Model):
    object_type = models.CharField(max_length=50, verbose_name="Тип объекта")

    def __str__(self):
        return self.object_type

class PaymentType(models.Model):
    payment_type = models.CharField(max_length=50, verbose_name="Тип платежа")

    def __str__(self):
        return self.payment_type

class MainContractors(models.Model):
    contractor = models.CharField(max_length=250, verbose_name="Основные партнеры")

    def __str__(self):
        return self.contractor

class ClientType(models.Model):
    type = models.CharField(max_length=50, verbose_name="Тип клиента")

    def __str__(self):
        return self.type