# Generated by Django 2.2.3 on 2019-10-09 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('owner_id',)},
        ),
        migrations.AlterField(
            model_name='project',
            name='manager_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_by_projectmanager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_by_projectowner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='status_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_by_project', to='project_status.ProjectStatus'),
        ),
    ]
