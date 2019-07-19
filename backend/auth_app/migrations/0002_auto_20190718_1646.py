# Generated by Django 2.2.3 on 2019-07-18 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(max_length=250, verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='father_name',
            field=models.CharField(max_length=50, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(max_length=250, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('photo', models.ImageField(blank=True, upload_to='uploads', verbose_name='Фото')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
