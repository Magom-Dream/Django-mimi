from rest_framework import serializers
from .models import Transaction
from accounts.models import Account

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('account', 'amount', 'updated_balance', 'transaction_details', 'transaction_type', 'transaction_method', 'transaction_time')
        read_only_fields = ('transaction_time',)