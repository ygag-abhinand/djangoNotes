# Generated by Django 4.2.4 on 2023-08-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
