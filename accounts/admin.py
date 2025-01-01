from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'bank_code', 'account_type', 'balance', 'user')
    search_fields = ('account_number', 'user__email')  # 유저 이메일로 검색 가능
