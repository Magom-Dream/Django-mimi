from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from accounts.models import Account
from rest_framework.permissions import IsAuthenticated


class TransactionCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            account = Account.objects.get(account_id=request.data.get('account'))
            if account.user != request.user:
                return Response({"error": "You can only create transactions for your own accounts."}, status=status.HTTP_403_FORBIDDEN)
            # 추가 로직: 잔액 확인, 입금/출금 여부 등
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(account__user=request.user)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

class TransactionRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id, account__user=request.user)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id, account__user=request.user)
            transaction.delete()
            return Response({"message": "Transaction deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)