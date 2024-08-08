from django.urls import path
from . import views
# from integrationapp.views import TaskStatusView


urlpatterns = [
    path('webhook/', views.IntegrationPayApiWeb.as_view(), name='webhook'),
    #path('task_status/<str:task_id>/', TaskStatusView.as_view(), name='task_status'),
]



