# Generated by Django 4.1.7 on 2023-03-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_rename_descriptiontext_comment_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='creation_date',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]
