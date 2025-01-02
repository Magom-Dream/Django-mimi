from rest_framework import serializers
from .models import Account
from django.contrib.auth import get_user_model

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('account_id', 'account_number', 'bank_code', 'account_type', 'balance', 'user')
        read_only_fields = ('account_id',)