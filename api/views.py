from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import File, TransferHistory
from django.core.exceptions import PermissionDenied, ValidationError
from django.contrib.auth.models import User
from django.utils.timezone import now

class TransferFileAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file_id = request.data.get('file_id')
        to_user_id = request.data.get('to_user_id')

        try:
            file = File.objects.get(id=file_id)
            to_user = User.objects.get(id=to_user_id)

            if file.owner != request.user:
                raise PermissionDenied("You are not the owner of this file.")

            file.owner = to_user
            file.save()

            TransferHistory.objects.create(
                file=file,
                from_user=request.user,
                to_user=to_user,
                action="TRANSFER",
                timestamp=now()
            )

            return Response({"message": "File transferred successfully."}, status=status.HTTP_200_OK)

        except File.DoesNotExist:
            return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "Recipient user not found."}, status=status.HTTP_404_NOT_FOUND)
        except PermissionDenied as e:
            return Response({"error": str(e)}, status=status.HTTP_403_FORBIDDEN)

class RevokeTransferAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file_id = request.data.get('file_id')

        try:
            file = File.objects.get(id=file_id)

            if file.owner != request.user:
                raise PermissionDenied("Only the current owner can revoke the transfer.")

            last_transfer = TransferHistory.objects.filter(file=file, action='TRANSFER').latest('timestamp')

            file.owner = last_transfer.from_user
            file.save()

            TransferHistory.objects.create(
                file=file,
                from_user=request.user,
                to_user=last_transfer.from_user,
                action="REVOKE",
                timestamp=now()
            )

            return Response({"message": "Transfer revoked successfully."}, status=status.HTTP_200_OK)

        except File.DoesNotExist:
            return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)
        except TransferHistory.DoesNotExist:
            return Response({"error": "No transfer history to revoke."}, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied as e:
            return Response({"error": str(e)}, status=status.HTTP_403_FORBIDDEN)
