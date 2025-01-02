from django.urls import path
from .views import AccountCreateView, AccountRetrieveDeleteView

urlpatterns = [
    path('accounts/', AccountCreateView.as_view(), name='account-create'),
    path('accounts/<uuid:account_id>/', AccountRetrieveDeleteView.as_view(), name='account-retrieve-delete'),
]