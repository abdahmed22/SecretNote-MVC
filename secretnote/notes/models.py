from django.db import models
from django.contrib.auth.models import User
# from cryptography.fernet import Fernet
# from django.conf import settings

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    
    # @property
    # def note_decrypted(self):
    #     f = Fernet(settings.ENCRYPTION_KEY)
    #     title_decrypted = f.decrypt(self.title)
    #     text_decrypted = f.decrypt(self.text)
    #     self.title = title_decrypted.decode('utf-8')
    #     self.text = text_decrypted.decode('utf-8')
    #     return self