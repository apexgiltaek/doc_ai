# Generated by Django 4.0.3 on 2022-03-25 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_info', '0013_remove_document_uploadtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file_path',
            field=models.FileField(blank=True, null=True, upload_to='Upload Files/'),
        ),
    ]