# from django.shortcuts import render
from integrationapp.serializers.serializers import IntegrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from integrationapp.services import IntegrationPayService
# from .Tasks.task import upload_payload, consume_queue
# from celery.result import AsyncResult
from rest_framework.permissions import IsAuthenticated
# import pika


class IntegrationPayApiWeb(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        serializer = IntegrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = IntegrationPayService(serializer.validated_data)
        obj = service.save_data()
  
        if obj:
            auth_eva = service.auth_eva_api()
            #upload = request.data
            #task = upload_payload.delay(upload)
            return Response(
                #{'task_id': task.id},
                {'Body': "Information Proccess"},
                status=status.HTTP_202_ACCEPTED
            )


# class TaskStatusView(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request, task_id):
#         body = consume_queue()
#         task = AsyncResult(task_id)
#         if task.state == 'PENDING':
#             response = {
#                 'status': task.state,
#                 'taskid': task_id,
#             }
#         elif task.state != 'FAILURE':
#             response = {
#                 'state': task.state,
#                 'result': task.result
#             }
#         else:
#             response = {
#                 'state': task.state,
#                 'status': str(task.info)  # this is the exception raised
#             }
#         return Response(response)


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'This is a protected view!'}
        return Response(content)
    