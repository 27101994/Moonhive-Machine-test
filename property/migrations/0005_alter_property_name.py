# Generated by Django 4.2.9 on 2024-02-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_delete_adminuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]