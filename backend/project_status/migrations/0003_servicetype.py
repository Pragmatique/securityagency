# Generated by Django 2.2.3 on 2019-10-02 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_status', '0002_propertytype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=50, verbose_name='Тип услуг')),
            ],
        ),
    ]
