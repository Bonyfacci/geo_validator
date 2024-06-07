from django.urls import path

from app_geo.apps import AppGeoConfig
from app_geo.views import AddressAPIView, RequestAPIView, HistoryAPIView, PingAPIView

app_name = AppGeoConfig.name


urlpatterns = [
    path('query/', AddressAPIView.as_view(), name='address'),
    path('result/<int:pk>/', RequestAPIView.as_view(), name='result_request'),
    path('history/', HistoryAPIView.as_view(), name='history_requests'),
    path('ping/', PingAPIView.as_view(), name='ping_check'),
]
