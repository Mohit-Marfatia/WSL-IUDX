from django.db import models

from django.contrib.auth.models import User
from django.db import models

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_files')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TransferHistory(models.Model):
    ACTION_CHOICES = [
        ('TRANSFER', 'Transfer'),
        ('REVOKE', 'Revoke'),
    ]

    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='transfer_history')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transferred_files')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_files')
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} | {self.file.name} | {self.from_user.username} -> {self.to_user.username}"
