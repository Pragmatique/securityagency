# Generated by Django 2.2.3 on 2019-10-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_status', '0004_objecttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainContractors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractor', models.CharField(max_length=50, verbose_name='Тип объекта')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(max_length=50, verbose_name='Тип объекта')),
            ],
        ),
    ]
