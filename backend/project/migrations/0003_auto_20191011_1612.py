# Generated by Django 2.2.3 on 2019-10-11 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20191009_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_by_project', to='client.Client'),
        ),
        migrations.AlterField(
            model_name='project',
            name='last_upd_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_by_lastupd', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='mounting_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mounting_by_project', to='mounting.Mounting'),
        ),
        migrations.AlterField(
            model_name='project',
            name='object_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='object_by_project', to='object.Object'),
        ),
        migrations.AlterField(
            model_name='project',
            name='payment_conditions_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paymentconditions_by_project', to='payment_conditions.PaymentConditions'),
        ),
        migrations.AlterField(
            model_name='project',
            name='service_type_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type_by_project', to='project_status.ServiceType'),
        ),
    ]
