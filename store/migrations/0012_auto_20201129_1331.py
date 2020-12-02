# Generated by Django 3.1.3 on 2020-11-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AlterField(
            model_name='product',
            name='about',
            field=models.CharField(blank=True, default='', max_length=500000, null=True),
        ),
    ]
