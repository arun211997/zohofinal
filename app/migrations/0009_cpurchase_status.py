# Generated by Django 5.0.2 on 2024-06-06 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_cpurchase_filters'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpurchase',
            name='status',
            field=models.TextField(null=True),
        ),
    ]