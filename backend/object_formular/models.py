from django.db import models
from auth_app.models import User


# Create your models here.
# Create your models here.
class ObjectFormular(models.Model):
    mounter_id = models.ForeignKey(User,
                                    related_name='by_objformular', on_delete=models.CASCADE, blank=True,
                                    verbose_name="Монтажор", null=True)
    control_panel_num = models.CharField(max_length=50, blank=True, verbose_name="Номер пульта")
    ppk_model = models.CharField(max_length=50, blank=True, verbose_name="Модель ППК")
    ppk_num = models.CharField(max_length=50, blank=True, verbose_name="Номер ППК")
    object_floor = models.PositiveIntegerField(blank=True, verbose_name="Этаж")
    max_floor = models.PositiveIntegerField(blank=True, verbose_name="Этажность")
    porch_num = models.PositiveIntegerField(blank=True, verbose_name="Подъезд")
    has_animals_flg = models.BooleanField(default=False, verbose_name="Есть животные")
    has_concierge_flg = models.BooleanField(default=False, verbose_name="Есть консьерж")
    has_intercom_flg = models.BooleanField(default=False, verbose_name="Есть домофон")
    has_code_doors_flg = models.BooleanField(default=False, verbose_name="Есть кодовые двери")
    has_windows_gratings_flg = models.BooleanField(default=False, verbose_name="Есть решетки на окнах")
    has_double_doors_flg = models.BooleanField(default=False, verbose_name="Есть двойные двери")
    has_keys_flg = models.BooleanField(default=False, verbose_name="Есть ключи")
    rooms_num = models.PositiveIntegerField(blank=True, verbose_name="Кол-во помещений")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('control_panel_num',)

    def __str__(self):
        return str(self.control_panel_num) + str(self.mounter_id)