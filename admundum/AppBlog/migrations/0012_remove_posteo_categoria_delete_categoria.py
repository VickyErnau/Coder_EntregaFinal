# Generated by Django 5.1.4 on 2025-01-23 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0011_remove_posteo_id_alter_posteo_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteo',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
