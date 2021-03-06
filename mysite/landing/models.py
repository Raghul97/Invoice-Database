from django.db import models

class UploadDocument(models.Model):
    invoice_number = models.CharField(max_length=25, blank=False)
    mobile_number = models.IntegerField(blank=False)
    document = models.FileField(blank=False)

class ViewDocument(models.Model):
    invoice_number = models.CharField(max_length=25, blank=False)