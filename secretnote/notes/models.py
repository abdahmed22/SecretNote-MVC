import datetime
from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings
from django.utils import timezone

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    destruction_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    secret = models.CharField(max_length=200, primary_key = True)
    
    @property
    def title_decrypted(self):
        f = Fernet(settings.ENCRYPTION_KEY)
        title_decrypted = f.decrypt(self.title)
        title = title_decrypted.decode('utf-8')
        return title
    
    @property
    def text_decrypted(self):
        f = Fernet(settings.ENCRYPTION_KEY)
        text_decrypted = f.decrypt(self.text)
        text = text_decrypted.decode('utf-8')
        return text
    
    @property
    def is_deleted(self):
        return timezone.now() > self.destruction_date