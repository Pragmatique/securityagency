from django.db import models
from project_status.models import PaymentType


# Create your models here.
# Create your models here.
class PaymentConditions(models.Model):
    payment_type = models.ForeignKey(PaymentType,
                                    related_name='by_payment_conditions', on_delete=models.CASCADE, blank=True,
                                    verbose_name="Способ оплаты")
    material_liability = models.PositiveIntegerField(blank=True, verbose_name="Материальная ответственность")
    base_payment = models.PositiveIntegerField(blank=True, verbose_name="Базовая оплата")
    extra_departure_value = models.PositiveIntegerField(blank=True, verbose_name="Стоимость дополнительного выезда")
    engeneer_ts_value = models.PositiveIntegerField(blank=True, verbose_name="Стоимость ТО инженера")
    sms_notification_value = models.PositiveIntegerField(blank=True, verbose_name="Стоимость СМС опопвещения")
    additional_channel_value = models.PositiveIntegerField(blank=True, verbose_name="Стоимость доп. канала связи")
    stayhome_value = models.PositiveIntegerField(blank=True, verbose_name="Стоимость услуги Остаюсь дома")
    extra_ensurance_value = models.PositiveIntegerField(blank=True, verbose_name="Стоимость доп. страховки")
    extra_detector_value = models.PositiveIntegerField(blank=True, verbose_name="Стоимость доп. датчика")
    operation_mode_value = models.PositiveIntegerField(blank=True, verbose_name="Стоимость Режим работы объекта")
    monthly_report_value = models.PositiveIntegerField(blank=True, verbose_name="Стоимость месячного отчета")
    alarm_button_value = models.PositiveIntegerField(blank=True, verbose_name="Стоимость Тревожной кнопки")
    duress_code_value = models.PositiveIntegerField(blank=True, verbose_name="Стоимость Код под принуждением")
    liqpay_subsription = models.BooleanField(default=False, verbose_name="Подписка liqpay")
    liqpay_subsription_date = models.DateField(blank=True, verbose_name="Начало подписки liqpay")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('base_payment',)

    def __str__(self):
        return self.base_payment