# Generated by Django 4.0.6 on 2023-02-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manga', '0008_alter_chapter_relase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='relase_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
