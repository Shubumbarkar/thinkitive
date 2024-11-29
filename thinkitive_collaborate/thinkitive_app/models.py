from django.db import models
class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    
    def __str__(self):
        return self.email
class Document(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True, default="")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
