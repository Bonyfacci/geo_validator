from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from app_geo.models import Request
from app_geo.serializers import AddressSerializer, RequestSerializer


@extend_schema(
    summary="Создать адрес",
)
class AddressAPIView(CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = AddressSerializer


@extend_schema(
    summary="Запросить результат",
)
class RequestAPIView(RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


@extend_schema(
    summary="Посмотреть историю",
)
class HistoryAPIView(ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = [SearchFilter]
    search_fields = ['address__cad_number']


@extend_schema(
    summary="Проверка работы сервера",
)
class PingAPIView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            message = 'Сервер запущен'
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = 'Сервер временно не работает'
            return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
