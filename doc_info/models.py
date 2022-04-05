from django.db import models


class Document(models.Model):
    doc_name = models.CharField(max_length=200)
    doc_type = models.CharField(max_length=50)
    file_path = models.FileField(upload_to="Upload Files/", null=True, blank=True)
    dateTimeOfUpload = models.DateTimeField(auto_now=True)
    original_YN = models.CharField(max_length=10)


class Object(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    obj_class = models.CharField(max_length=50, null=True, blank=True)
    obj_content = models.TextField(blank=True)
    LB_x = models.FloatField(null=True, blank=True)
    LB_y = models.FloatField(null=True, blank=True)
    RT_x = models.FloatField(null=True, blank=True)
    RT_y = models.FloatField(null=True, blank=True)

