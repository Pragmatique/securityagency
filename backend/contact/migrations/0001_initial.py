# Generated by Django 2.2.3 on 2019-10-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=200, verbose_name='Имя')),
                ('father_name', models.CharField(blank=True, max_length=200, verbose_name='Отчество')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='Город')),
                ('street', models.CharField(blank=True, max_length=100, verbose_name='Улица')),
                ('house_num', models.PositiveIntegerField(blank=True, verbose_name='Номер дома')),
                ('flat_num', models.PositiveIntegerField(blank=True, verbose_name='Номер квартиры')),
                ('phone', models.CharField(max_length=200, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, db_index=True, max_length=200, verbose_name='Емейл')),
                ('date_birth', models.DateField(blank=True, verbose_name='Дата рождения')),
                ('tax_number', models.CharField(blank=True, max_length=10, verbose_name='ИНН')),
                ('passport_number', models.CharField(blank=True, max_length=7, verbose_name='Пасспорт')),
                ('position', models.CharField(blank=True, max_length=200, verbose_name='Должность')),
                ('photo', models.ImageField(blank=True, upload_to='contacts/', verbose_name='Фото')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('last_name',),
            },
        ),
    ]
