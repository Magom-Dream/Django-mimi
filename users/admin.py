from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 목록에서 표시할 필드들 설정(어드민 목록 페이지에서 보여줄 필드들)
    list_display = ('email', 'name', 'nickname', 'phone_number', 'is_active', 'is_staff', 'last_login')
    
    # 필터링을 할 수 있는 필드들 설정(어드민 페이지에서 필터링할 수 있는 필드)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    
    # 검색 기능 추가
    search_fields = ('email', 'name', 'nickname', 'phone_number')
    
    # 상세보기에서 보여줄 필드들 설정(어드민 세부 정보 페이지에서 보여줄 필드들)
    fields = ('email', 'name', 'nickname', 'phone_number', 'is_active', 'is_staff', 'is_superuser', 'last_login')
    
    # 수정할 수 없는 필드 설정 (예: last_login)
    readonly_fields = ('last_login', 'is_staff', 'is_superuser',)
    

    # 기본 정렬 설정
    ordering = ('email',)
