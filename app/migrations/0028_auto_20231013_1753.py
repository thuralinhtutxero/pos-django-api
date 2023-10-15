# Generated by Django 3.2.9 on 2023-10-13 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AddField(
            model_name='sales',
            name='totalProfit',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='soldproduct',
            name='profit',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
