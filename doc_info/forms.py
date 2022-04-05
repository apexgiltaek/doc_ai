from django import forms
from doc_info.models import Document, Object


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['doc_type', 'file_path', 'original_YN']
        labels = {
            'doc_type': '문서 종류',
            'file_path': '문서 경로',
            'original_YN': '원본 식별',
        }


class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ['obj_class', 'obj_content', 'LB_x', 'LB_y', 'RT_x', 'RT_y']
        labels = {
            'obj_class': '분류',
            'obj_content': '내용',
            'LB_x': '좌하단x',
            'LB_y': '좌하단y',
            'RT_x': '우상단x',
            'RT_y': '우상단y',
        }
