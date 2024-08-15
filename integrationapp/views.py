from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from integrationapp.serializers.serializers import IntegrationSerializer
from integrationapp.services import IntegrationPayService


class IntegrationPayApiWeb(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        datapayload = request.data
        serializer = IntegrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = IntegrationPayService(serializer.validated_data)
        object = service.save_data()
        payloadid = object.id
        if object:
            auth_eva = service.auth_eva_api()
            if auth_eva:
                cookiestring = str(auth_eva[0])
                save_payload_eva = service.save_payload_eva(datapayload,
                                                            cookiestring)
                if Response(save_payload_eva == 200):
                    print(save_payload_eva)
                    update_status_payment = service.update_status(payloadid,
                                                                  'Approved'
                                                                  )
                    print(f"Update Status {update_status_payment}")
                    return Response(save_payload_eva.json())


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {"message": "This is a protected view!"}
        return Response(content)
