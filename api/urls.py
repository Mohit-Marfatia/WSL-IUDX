from django.urls import path
from .views import TransferFileAPI, RevokeTransferAPI

urlpatterns = [
    path('transfer/', TransferFileAPI.as_view(), name='transfer_file'),
    path('revoke/', RevokeTransferAPI.as_view(), name='revoke_transfer'),
]
