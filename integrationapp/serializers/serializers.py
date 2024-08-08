from rest_framework import serializers

from integrationapp.models.IntegrationPayment.models import IntegrationPaymentsProvider

   
class PaymentPeriodsSerializer(serializers.Serializer):
    periodStartDate = serializers.DateField()
    periodEndDate = serializers.DateField()
    paidAmount = serializers.FloatField()
    
   
class IntegrationSerializer(serializers.ModelSerializer):
    paymentPeriods = PaymentPeriodsSerializer(many=True)

    class Meta:
        model = IntegrationPaymentsProvider
        fields = [
            "policyNumber",
            "transactionDate",
            "transactionId",
            "paymentMethod",
            "sendNotification",
            "paymentDescription",
            "totalPaid",
            "providerName",
            "paymentPeriods",
        ]
