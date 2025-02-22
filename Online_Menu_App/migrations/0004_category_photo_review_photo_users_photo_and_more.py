# Generated by Django 5.0 on 2024-10-25 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Menu_App', '0003_menuitem_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='review',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='users',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Online_Menu_App.order'),
        ),
    ]
