from django.urls import path
from . import views
# from integrationapp.views import TaskStatusView


urlpatterns = [
    path('payintegration/', views.IntegrationPayApiWeb.as_view(),
         name='payintegration'),
]
