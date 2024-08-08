from integrationapp.models.IntegrationPayment.models import IntegrationPaymentsProvider
import json


class IntegrationPayService:
    def __init__(self, ser):
        self.ser = ser

    def save_data(self):
        policy = self.ser["policyNumber"]
        Datetransaction = self.ser["transactionDate"]
        Idtransaction = self.ser["transactionId"]
        Methodpayment = self.ser["paymentMethod"]
        Notification = self.ser["sendNotification"]
        DescriptionPay = self.ser["paymentDescription"]
        Paid = self.ser["totalPaid"]
        NameProvider = self.ser["providerName"]
        periods = json.dumps(self.ser["paymentPeriods"], default=str)
        payload = json.dumps(self.ser, default=str)

        obj = IntegrationPaymentsProvider.objects.create(
            policyNumber=policy,
            transactionDate=Datetransaction,
            transactionId=Idtransaction,
            paymentMethod=Methodpayment,
            sendNotification=Notification,
            paymentDescription=DescriptionPay,
            totalPaid=Paid,
            providerName=NameProvider,
            paymentPeriods=periods,
            payload=payload,
        )
        return obj
