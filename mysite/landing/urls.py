from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('upload/', views.upload_document, name='upload_document'),
    path('view/', views.view_document, name='view_document'),
    path('upload/success/', views.success, name='success'),
]
