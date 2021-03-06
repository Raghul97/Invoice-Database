from django.forms import ModelForm
from .models import UploadDocument, ViewDocument

class UploadDocumentForm(ModelForm):
    class Meta:
        model = UploadDocument
        fields = ['invoice_number', 'mobile_number', 'document' ]

class ViewDocumentForm(ModelForm):
    class Meta:
        model = ViewDocument
        fields = ['invoice_number']