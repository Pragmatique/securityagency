from django.db import models
from contact.models import Contact
from auth_app.models import User
from object.models import Object
from client.models import Client
from mounting.models import Mounting
from payment_conditions.models import PaymentConditions
from project_status.models import ProjectStatus, ServiceType


# Create your models here.
class Project(models.Model):
    status_id = models.ForeignKey(ProjectStatus,
                                 related_name='status_by_project', on_delete=models.CASCADE)
    owner_id = models.ForeignKey(User,
                                related_name='user_by_projectowner', on_delete=models.CASCADE)
    manager_id = models.ForeignKey(User,
                                 related_name='user_by_projectmanager', on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client,
                                   related_name='client_by_project', on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.ForeignKey(Object,
                                  related_name='object_by_project', on_delete=models.CASCADE, blank=True, null=True)
    mounting_id = models.ForeignKey(Mounting,
                                  related_name='mounting_by_project', on_delete=models.CASCADE, blank=True, null=True)
    last_upd_by = models.ForeignKey(User,
                                   related_name='user_by_lastupd', on_delete=models.CASCADE, blank=True, null=True)
    service_type_id = models.ForeignKey(ServiceType,
                                    related_name='type_by_project', on_delete=models.CASCADE, blank=True, null=True)
    payment_conditions_id = models.ForeignKey(PaymentConditions,
                                    related_name='paymentconditions_by_project', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('owner_id',)

    def __str__(self):
        return str(self.owner_id)