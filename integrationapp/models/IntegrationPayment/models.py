from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True,
        db_table = 'integration_payments_provider'


class IntegrationPaymentsProvider(BaseModel):
    policyNumber = models.CharField(max_length=50)
    transactionDate = models.DateField(max_length=50)
    transactionId = models.CharField(max_length=50)
    paymentMethod = models.CharField(max_length=50)
    sendNotification = models.BooleanField(False)
    paymentDescription = models.CharField(max_length=500)
    totalPaid = models.FloatField()
    providerName = models.CharField(max_length=200, default="name provider")
    status = models.CharField(
        max_length=8,
        default="PENDING",
    )
    pkintegrationevastatus = models.CharField(
        max_length=200,
        default="without information",
    )
    paymentPeriods = models.CharField(max_length=5000)
    payload = models.CharField(max_length=5000)
