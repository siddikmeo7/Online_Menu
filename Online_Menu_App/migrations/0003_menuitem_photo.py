# Generated by Django 5.0 on 2024-10-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Menu_App', '0002_category_menuitem_order_orderitem_review_users_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='photo',
            field=models.ImageField(null=True, upload_to='static/images'),
        ),
    ]
