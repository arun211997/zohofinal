# Generated by Django 5.0.2 on 2024-06-04 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_tripnumber_orderno_ordernumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpurchase',
            name='filters',
            field=models.TextField(null=True),
        ),
    ]
