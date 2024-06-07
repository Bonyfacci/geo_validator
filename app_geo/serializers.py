import requests
from rest_framework import serializers

from base.choises import RequestStatusChoice
from .models import Address, Request


class AddressSerializer(serializers.ModelSerializer):
    response = serializers.CharField(read_only=True)

    class Meta:
        model = Address
        fields = ['cad_number', 'latitude', 'longitude', 'response']

    def create(self, validated_data):
        address = Address.objects.create(**validated_data)
        data = {
            'cad_number': address.cad_number,
            'latitude': float(address.latitude),
            'longitude': float(address.longitude)
        }
        response = requests.post('http://localhost:8000/rus_registry/', data=data)
        Request.objects.create(address=address, response=response.json()['response'])
        if 'response' in response.json():
            address.response = RequestStatusChoice(response.json()['response']).label
        else:
            address.response = 'Ошибка сервера'
        address.save()
        return AddressSerializer(address).data


class RequestSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Request
        fields = ['address', 'created', 'updated', 'response']


class PingSerializer(serializers.ModelSerializer):
    pass
