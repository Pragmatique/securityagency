from django.db import models
from project_status.models import MainContractors, PaymentType


# Create your models here.
# Create your models here.
class Mounting(models.Model):
    contractor_id = models.ForeignKey(MainContractors,
                                    related_name='contractor_by_mounting', on_delete=models.CASCADE, blank=True,
                                    verbose_name="Компания на монтаж", null=True)
    mounting = models.CharField(max_length=50, default="Монтаж", verbose_name="Монтаж")
    object_inspection = models.BooleanField(default=False, verbose_name="Осмотр объекта")
    payment_type_id = models.ForeignKey(PaymentType,
                                    related_name='type_by_mounting', on_delete=models.CASCADE, blank=True,
                                    verbose_name="Способ оплаты", null=True)
    estimate = models.PositiveIntegerField(blank=True, verbose_name="Смета")
    mounting_value = models.PositiveIntegerField(blank=True, verbose_name="Сумма за монтаж")
    mounting_income = models.PositiveIntegerField(blank=True, verbose_name="Доход от монтажа")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('mounting_income',)

    def __str__(self):
        return self.mounting_income