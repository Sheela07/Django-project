from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
import requests
from requests.exceptions import RequestException

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

@api_view(['GET'])
def get_destinations_for_account(request, account_id):
    account = get_object_or_404(Account, account_id=account_id)
    destinations = account.destinations.all()
    serializer = DestinationSerializer(destinations, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def incoming_data(request):
    app_secret_token = request.headers.get('CL-X-TOKEN')
    if not app_secret_token:
        return Response({'error': 'Un Authenticate'}, status=status.HTTP_401_UNAUTHORIZED)
    
    account = get_object_or_404(Account, app_secret_token=app_secret_token)
    data = request.data

    if not isinstance(data, dict):
        return Response({'error': 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)
    
    for destination in account.destinations.all():
        headers = destination.headers if destination.headers else {}
        try:
            if destination.http_method == 'GET':
                response = requests.get(destination.url, headers=headers, params=data)
            elif destination.http_method == 'POST':
                response = requests.post(destination.url, headers=headers, json=data)
            elif destination.http_method == 'PUT':
                response = requests.put(destination.url, headers=headers, json=data)
            
            response.raise_for_status()  # Raise an error for bad HTTP status codes

        except RequestException as e:
            return Response({'error': f'Failed to send data to destination: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({'success': 'Data sent to all destinations'}, status=status.HTTP_200_OK)