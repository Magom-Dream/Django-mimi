from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'transaction_type', 'amount', 'transaction_method', 'transaction_time')
    list_filter = ('transaction_type', 'transaction_method', 'transaction_time')
    search_fields = ('account__account_number', 'transaction_type')