# Generated by Django 4.0.3 on 2022-03-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_info', '0002_rename_obj_name_object_obj_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='obj_content',
            field=models.TextField(),
        ),
    ]
