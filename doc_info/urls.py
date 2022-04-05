from django.urls import path
from . import views

app_name = 'doc_info'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:document_id>/', views.detail, name='detail'),
    path('object/create/<int:document_id>/', views.object_create, name='object_create'),
    path('document/create/', views.document_create, name='document_create'),
    path('document/modify/<int:document_id>/', views.document_modify, name='document_modify'),
    path('document/delete/<int:document_id>/', views.document_delete, name='document_delete'),
    path('object/modify/<int:object_id>/', views.object_modify, name='object_modify'),
    path('object/delete/<int:object_id>/', views.object_delete, name='object_delete'),
]
