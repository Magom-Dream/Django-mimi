from django.urls import path
from .views import TransactionCreateView, TransactionListView, TransactionRetrieveUpdateDeleteView

urlpatterns = [
    path('transactions/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transactions/list/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/<int:transaction_id>/', TransactionRetrieveUpdateDeleteView.as_view(), name='transaction-retrieve-update-delete'),
]