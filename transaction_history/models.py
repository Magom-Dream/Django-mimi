from django.db import models
from accounts.models import Account

# 거래 타입
TRANSACTION_TYPE = [
    ("DEPOSIT", "입금"),
    ("WITHDRAW", "출금"),
]

# 거래 종류
TRANSACTION_METHOD = [
    ("ATM", "ATM 거래"),
    ("TRANSFER", "계좌이체"),
    ("AUTOMATIC_TRANSFER", "자동이체"),
    ("CARD", "카드결제"),
    ("INTEREST", "이자"),
]

class Transaction(models.Model):
    # account: 거래와 연결된 계좌 정보, 계좌가 삭제되면 거래도 삭제됨 (CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_index=True)
    # amount: 거래 금액, 소수점 이하 2자리까지 허용
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    # updated_balance: 거래 후 계좌의 잔액, 소수점 이하 2자리까지 허용
    updated_balance = models.DecimalField(max_digits=15, decimal_places=2)
    # transaction_details: 거래 상세 설명, 선택적으로 입력 가능 (빈 값 허용)
    transaction_details = models.CharField(max_length=255, blank=True)
    # transaction_type: 거래 유형, DEPOSIT(입금) 또는 WITHDRAW(출금) 중 하나를 선택
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE)
    # transaction_method: 거래 방법, TRANSACTION_METHOD에서 정의된 항목 중 하나를 선택
    transaction_method = models.CharField(max_length=20, choices=TRANSACTION_METHOD)
    # transaction_time: 거래 발생 시간, 생성 시 자동으로 현재 시간이 설정되며 데이터베이스 인덱스 추가
    transaction_time = models.DateTimeField(auto_now_add=True, db_index=True)

    # __str__: Transaction 객체를 문자열로 표현
    def __str__(self):
        # 객체를 출력할 때 계좌, 거래 유형, 금액, 거래 방법, 거래 시간을 포함한 형식으로 반환
        return (
            f"Account: {self.account}, "
            f"Type: {self.get_transaction_type_display()}, "
            f"Amount: {self.amount}, "
            f"Method: {self.get_transaction_method_display()}, "
            f"Time: {self.transaction_time}"
        )
