from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    file = models.FileField()
    logo = models.ImageField(default="pdflogo.png", null=True, blank=True)
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
    @property
    def ImageURL(self):
            try:
                url = self.logo.url
            except:
                url = ''
            return url

class ExtractedText(models.Model):
    file = models.ForeignKey(Document, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)


    def __str__(self) -> str:
         return self.title