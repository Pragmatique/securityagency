from django.db import models

# Create your models here.
class ProjectStatus(models.Model):
    status = models.CharField(max_length=50, verbose_name="Статус")

class PropertyType(models.Model):
    property_type = models.CharField(max_length=50, verbose_name="Тип собственности")

class ServiceType(models.Model):
    service_type = models.CharField(max_length=50, verbose_name="Тип услуг")

class ObjectType(models.Model):
    object_type = models.CharField(max_length=50, verbose_name="Тип объекта")

class PaymentType(models.Model):
    payment_type = models.CharField(max_length=50, verbose_name="Тип платежа")

class MainContractors(models.Model):
    contractor = models.CharField(max_length=250, verbose_name="Основные партнеры")

class ClientType(models.Model):
    type = models.CharField(max_length=50, verbose_name="Тип клиента")