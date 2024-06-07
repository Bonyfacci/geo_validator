from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app_geo.services import emulate_sending


@extend_schema(
    summary="Эмуляция сервера Росреестра",
)
class RusRegistryServerView(APIView):

    def post(self, request):
        if request.data:
            address = request.data
            response = emulate_sending()
            return Response({'response': response}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid request data'}, status=status.HTTP_400_BAD_REQUEST)
