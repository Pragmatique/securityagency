# Generated by Django 2.2.3 on 2019-10-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(max_length=50, verbose_name='Тип собственности')),
            ],
        ),
    ]
