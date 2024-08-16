from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from integrationapp.serializers.serializers import IntegrationSerializer
from integrationapp.services import IntegrationPayService
import json
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import status


class IntegrationPayApiWeb(APIView):

    def post(self, request, *args, **kwargs):
        datapayload = request.data
        serializer = IntegrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = IntegrationPayService(serializer.validated_data)
        object = service.save_data()
        payloadid = object.id
        auth_eva = service.auth_eva_api()
        cookiestring = str(auth_eva[0])
        save_payload_eva = service.save_payload_eva(datapayload,
                                                    cookiestring
                                                    )
        if (save_payload_eva.status_code == 200):
            paymentresult = save_payload_eva.text
            payment_status = json.loads(paymentresult)
            data_dict = payment_status['data']
            obj_id = data_dict.get('id')
            obj_status = data_dict.get('status')
            service.update_status(payloadid, obj_status, obj_id)
            return Response(save_payload_eva.json(),
                            status=status.HTTP_200_OK)
        elif save_payload_eva.status_code == 400:
            return Response(save_payload_eva.json(),
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(save_payload_eva.json(),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegisterUserAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password are required'},
                            status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username,
                                        password=password)
        user.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
