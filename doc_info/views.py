from .models import Document, Object
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DocumentForm, ObjectForm
from django.db.models import Q
from .ai import object_ai
from django.utils import timezone

import os

def index(request):
    kw = request.GET.get('kw', '')
    page = request.GET.get('page', '1')
    so = request.GET.get('so', '')

    document_list = Document.objects.all()

    if so:
        if so == '전체':
            document_list = Document.objects.all()
        else:
            document_list = document_list.filter(
                Q(doc_type__icontains=so)
            ).distinct()

    if kw:
        document_list = document_list.filter(
            Q(doc_name__icontains=kw)
        ).distinct()

    paginator = Paginator(document_list, 10)
    page_obj = paginator.get_page(page)

    context = {'document_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'doc_info/document_list.html', context)


def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    context = {'document': document}
    return render(request, 'doc_info/document_detail.html', context)


def object_create(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    document.object_set.create(obj_content=request.POST.get('obj_content'),
                               obj_class=request.POST.get('obj_class'),
                               LB_x=request.POST.get('LB_x'),
                               LB_y=request.POST.get('LB_y'),
                               RT_x=request.POST.get('RT_x'),
                               RT_y=request.POST.get('RT_y')
                               )
    return redirect('doc_info:detail', document_id=document.id)


def document_create(request):
    if request.method == 'POST':
        doc_type = request.POST['doc_type']
        file_path = request.FILES['file_path']
        original_YN = request.POST['original_YN']
        documentCreate = Document(
            doc_name = os.path.basename(str(file_path)),
            doc_type=doc_type,
            file_path=file_path,
            original_YN=original_YN,
        )
        documentCreate.save()
        print(str(file_path))
        for i in object_ai(str(file_path)):
            documentCreate.object_set.create(obj_content=i[4],
                                       obj_class='',
                                       LB_x=i[0],
                                       LB_y=i[1],
                                       RT_x=i[2],
                                       RT_y=i[3],
                                       )
        return redirect('doc_info:index')
    else:
        documentform = DocumentForm
        context = {
            'documentform': documentform,
        }
    return render(request, 'doc_info/document_form.html', context)


def document_modify(request, document_id):
    document = get_object_or_404(Document, pk=document_id)

    if request.method == "POST":
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            document = form.save(commit=False)
            document.save()
            return redirect('doc_info:detail', document_id=document.id)
    else:
        form = DocumentForm(instance=document)
    context = {'form': form}
    return render(request, 'doc_info/document_form.html', context)


def document_delete(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    document.delete()
    return redirect('doc_info:index')


def object_modify(request, object_id):
    object = get_object_or_404(Object, pk=object_id)

    if request.method == "POST":
        form = ObjectForm(request.POST, instance=object)
        if form.is_valid():
            object = form.save(commit=False)
            object.save()
            return redirect('doc_info:detail', document_id=object.document.id)
    else:
        form = ObjectForm(instance=object)
    context = {'form':form}
    return render(request, 'doc_info/object_form.html', context)


def object_delete(request, object_id):
    object = get_object_or_404(Object, pk=object_id)
    object.delete()
    return redirect('doc_info:detail', document_id=object.document.id)

