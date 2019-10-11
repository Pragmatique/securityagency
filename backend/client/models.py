from django.db import models
from contact.models import Contact
from project_status.models import ClientType

# Create your models here.
class Client(models.Model):
    contact_id = models.ForeignKey(Contact,
                                 related_name='client', on_delete=models.CASCADE, blank=True, null=True)
    company_name = models.CharField(max_length=200, verbose_name="Название компании", blank=True)
    channel = models.CharField(max_length=200, blank=True, verbose_name="Канал захода")
    referal_program = models.CharField(max_length=200, blank=True, verbose_name="Реферальная программа")
    client_type = models.ForeignKey(ClientType,
                                    related_name='clients', blank=True, on_delete=models.CASCADE, null=True)
    city = models.CharField(max_length=50, blank=True, verbose_name="Город")
    street = models.CharField(max_length=100, blank=True, verbose_name="Улица")
    house_num = models.PositiveIntegerField(blank=True, verbose_name="Номер дома")
    flat_num = models.PositiveIntegerField(blank=True, verbose_name="Номер квартиры")
    phone = models.CharField(max_length=200, verbose_name="Телефон")
    email = models.EmailField(max_length=200, blank=True, db_index=True, verbose_name="Емейл")
    tax_number = models.CharField(max_length=10, blank=True, verbose_name="ЕГРПО")
    network_cl_5plus = models.BooleanField(default= False, verbose_name="Сетевой клиент 5+")
    network_cl_20plus = models.BooleanField(default= False, verbose_name="Сетевой клиент 20+")
    balance_1c = models.IntegerField(blank=True, verbose_name="Баланс 1С")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('company_name',)

    def __str__(self):
        return self.company_name