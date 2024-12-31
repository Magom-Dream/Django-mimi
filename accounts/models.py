from django.db import models
from django.conf import settings 
import uuid
from django.core.exceptions import ValidationError

# 은행 코드 선택지 (constants.py 파일에서 가져와야 함)
BANK_CODES = [
    ("001", "국민은행"),
    ("002", "농협은행"),
    ("003", "우리은행"),
    ("004", "전북은행"),
    ("005", "신한은행"),
    ("006", "카카오뱅크"),
    ("007", "토스뱅크"),
]

# 계좌 종류 선택지
ACCOUNT_TYPES = [
    ('CHECKING', '입출금'),
    ('OVERDRAFT', '마이너스'),
    ("SAVING", "적금"),
    ("LOAN", "대출"),
    ("PENSION", "연금"),
    ("STOCK", "주식"),
]

class Account(models.Model):
    # 기본 키: UUID 사용
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 유저 정보: 외래 키로 연결하기
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='accounts')

    # 계좌번호
    account_number = models.CharField(max_length=20, unique=True)
    def clean(self): # 계좌번호는 숫자만 허용
        super().clean()
        if not self.account_number.isdigit():
            raise ValidationError("계좌번호는 숫자만 포함해야 합니다.")

    # 은행 코드
    bank_code = models.CharField(max_length=10, choices=BANK_CODES)

    # 계좌 종류
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)

    # 잔액
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    # 문자열 표현
    def __str__(self):
        return f"Account {self.account_number} ({self.bank_code})"