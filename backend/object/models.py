from django.db import models
from project_status.models import PropertyType, ObjectType
from client.models import Client
from contact.models import Contact
# Create your models here.

class Object(models.Model):
    client_id = models.ForeignKey(Client,
                                    related_name='objects_by_client', on_delete=models.CASCADE, blank=True,
                                    verbose_name="Клиент", null=True)
    property_type_id = models.ForeignKey(PropertyType,
                                    related_name='objects_by_property', on_delete=models.CASCADE, blank=True,
                                    verbose_name="Тип собственности", null=True)
    object_type_id = models.ForeignKey(ObjectType,
                                    related_name='objects_by_type', on_delete=models.CASCADE, blank=True,
                                    verbose_name="Тип обьекта", null=True)
    city = models.CharField(max_length=50, blank=True, verbose_name="Город")
    street = models.CharField(max_length=100, blank=True, verbose_name="Улица")
    house_num = models.PositiveIntegerField(blank=True, verbose_name="Номер дома")
    flat_num = models.PositiveIntegerField(blank=True, verbose_name="Номер квартиры")
    rel_person1 = models.ForeignKey(Contact,
                                    related_name='objects_by_contact1', on_delete=models.CASCADE, blank=True,
                                    verbose_name="Связанное лицо1", null=True)
    rel_person2 = models.ForeignKey(Contact,
                                    related_name='objects_by_contact2', on_delete=models.CASCADE, blank=True,
                                    verbose_name="Связанное лицо2", null=True)
    rel_person3 = models.ForeignKey(Contact,
                                    related_name='objects_by_contact3', on_delete=models.CASCADE, blank=True,
                                    verbose_name="Связанное лицо3", null=True)
    rel_person4 = models.ForeignKey(Contact,
                                    related_name='objects_by_contact4', on_delete=models.CASCADE, blank=True,
                                    verbose_name="Связанное лицо4", null=True)
    date_first_reation = models.DateField(blank=True, verbose_name="Дата первой реакции")
    denying_password = models.CharField(max_length=200, verbose_name="Пароль подтверждения отмены", blank=True)
    additional_services = models.CharField(max_length=200, blank=True, verbose_name="Дополнительные сервисы")
    scan_main_deal = models.ImageField(upload_to='main_deals/', blank=True, verbose_name="Скан основного договора")
    scan_mounting_deal = models.ImageField(upload_to='mounting_deals/', blank=True, verbose_name="Скан монтажного договора")
    verified_deal_flg = models.BooleanField(default=False, verbose_name="Флаг подтверждения договора")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('street',)

    def __str__(self):
        return self.street + ' ' + self.house_num + ',' + self.flat_num
