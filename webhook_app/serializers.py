from rest_framework import serializers
from .models import Account, Destination

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'account_id', 'account_name', 'app_secret_token', 'website']

class DestinationSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)  # If you want nested representation

    class Meta:
        model = Destination
        fields = ['account', 'url', 'http_method', 'headers']

# Optionally, if you want to include the account_id instead of a nested representation
class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['account', 'url', 'http_method', 'headers']
        extra_kwargs = {
            'account': {'write_only': True}
        }
