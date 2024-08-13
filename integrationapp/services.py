from integrationapp.models.IntegrationPayment.models import IntegrationPaymentsProvider
import json
import requests
from integrationapp.constants import (EVA_LOGIN_URL,
                                      HEADERS_LOGIN,
                                      DATA_ACCESS_LOGIN,
                                      EVA_URL_PAYMENT,
                                      HEADERS_PAYMENT)


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
        #NameProvider = self.ser["providerName"]
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
            #providerName=NameProvider,
            paymentPeriods=periods,
            payload=payload,
        )
        return obj

    def auth_eva_api(self):
        url = EVA_LOGIN_URL
        headers = HEADERS_LOGIN
        data = DATA_ACCESS_LOGIN
        response = requests.post(url, json=data,
                                 headers=headers,
                                 )
        headersito = response.headers.get('Set-Cookie', '')
        print(headersito)
        headersresponse = response.headers.get('Set-Cookie', '').split(';')
        return headersresponse

    def save_payload_eva(self, payload, cookie):
        cookiesion = cookie
        cookieString = str(cookiesion)
        urlpay = EVA_URL_PAYMENT
        headerspay = HEADERS_PAYMENT
        headerspay["Cookie"] = cookieString
        body = payload
        print(headerspay)
        responsepay = requests.post(urlpay, json=body,
                                    headers=headerspay,
                                    )
        bodyresponse = responsepay
        print(f"Header Response: {bodyresponse}")
        return bodyresponse