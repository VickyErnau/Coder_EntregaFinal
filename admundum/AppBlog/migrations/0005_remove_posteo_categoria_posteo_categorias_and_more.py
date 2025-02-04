# Generated by Django 5.1.4 on 2025-01-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0004_remove_posteo_categorias_posteo_categoria_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteo',
            name='categoria',
        ),
        migrations.AddField(
            model_name='posteo',
            name='categorias',
            field=models.ManyToManyField(related_name='posts', to='AppBlog.categoria'),
        ),
        migrations.RemoveField(
            model_name='posteo',
            name='autor',
        ),
        migrations.AddField(
            model_name='posteo',
            name='autor',
            field=models.ManyToManyField(related_name='posts', to='AppBlog.autor'),
        ),
    ]
