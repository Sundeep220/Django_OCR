from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Document(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.file.name

    @property
    def fileURL(self):
            try:
                url = self.file.url
            except:
                url = ''
            return url

# class ExtractedText(models.Model):
#     filename = models.OneToOneField(Document, on_delete=models.CASCADE, null=True)
#     text = models.TextField(null=True, blank=True)