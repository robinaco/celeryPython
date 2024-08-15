from integrationapp.models.IntegrationPayment.models import IntegrationPaymentsProvider
import json
import requests
from rest_framework.response import Response
from rest_framework import status
from integrationapp.constants import (
    EVA_LOGIN_URL,
    HEADERS_LOGIN,
    DATA_ACCESS_LOGIN,
    EVA_URL_PAYMENT,
    HEADERS_PAYMENT,
)


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
            paymentPeriods=periods,
            payload=payload,
        )
        return obj

    def auth_eva_api(self):
        url = EVA_LOGIN_URL
        headers = HEADERS_LOGIN
        data = DATA_ACCESS_LOGIN
        response = requests.post(
            url,
            json=data,
            headers=headers,
        )
        if response.status_code == 200:
            return response.headers.get("Set-Cookie", "").split(";")
        else:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

    def save_payload_eva(self, payload, cookie):
        HEADERS_PAYMENT["Cookie"] = str(cookie)
        return requests.post(EVA_URL_PAYMENT,
                             json=payload,
                             headers=HEADERS_PAYMENT
                             )
        
    def update_status(self, payloadid, state):
        try:
            instance = IntegrationPaymentsProvider.objects.get(id=payloadid)
            print(instance)
        except IntegrationPaymentsProvider.DoesNotExist:
            return Response({'error': 'Not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = IntegrationPaymentsProvider(instance)
        print(serializer.status)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
