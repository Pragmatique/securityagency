from django.db import models

# Create your models here.

class Contact(models.Model):

    first_name = models.CharField(max_length=200, db_index=True, verbose_name="Имя")
    father_name = models.CharField(max_length=200, blank=True, verbose_name="Отчество")
    last_name = models.CharField(max_length=200, verbose_name="Фамилия")
    city = models.CharField(max_length=50, blank=True, verbose_name="Город")
    street = models.CharField(max_length=100, blank=True, verbose_name="Улица")
    house_num = models.PositiveIntegerField(blank=True, verbose_name="Номер дома")
    flat_num = models.PositiveIntegerField(blank=True, verbose_name="Номер квартиры")
    phone = models.CharField(max_length=200, verbose_name="Телефон")
    email = models.EmailField(max_length=200, blank=True, db_index=True, verbose_name="Емейл")
    date_birth = models.DateField(blank=True, verbose_name="Дата рождения")
    tax_number = models.CharField(max_length=10, blank=True, verbose_name="ИНН")
    passport_number = models.CharField(max_length=7, blank=True, verbose_name="Пасспорт")
    position = models.CharField(max_length=200, blank=True, verbose_name="Должность")
    photo = models.ImageField(upload_to='contacts/',blank=True, verbose_name="Фото")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        return self.last_name + self.first_name
