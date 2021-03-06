from django.shortcuts import render, redirect
from .forms import UploadDocumentForm, ViewDocumentForm
from django.http import HttpResponse
from .models import UploadDocument

def index(request):
    return render(request, template_name='index.html')

def success(request):
    return render(request, 'success.html')

def upload_document(request):
    if request.method == 'POST':
        form = UploadDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UploadDocumentForm()
    return render(request, 'upload.html', { 'form': form } )

def view_document(request):
    data = {}
    if request.method == 'POST':
        form = ViewDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                invoice = UploadDocument.objects.get(invoice_number=request.POST['invoice_number'])
                data['invoice_number'] = request.POST['invoice_number']
                data['mobile_number'] = invoice.mobile_number
                data['url'] = invoice.document.url
                return render(request, 'view.html', { 'form': form, 'data': data } )
            except:
                return HttpResponse("<h2>Invalid Invoice Number or Invoice Number Not Uploaded Yet.</h2>")
    else:
        form = ViewDocumentForm()
    return render(request, 'view.html', { 'form': form, 'data': data } )