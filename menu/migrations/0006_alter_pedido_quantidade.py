# Generated by Django 4.1.7 on 2024-06-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_pedido_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='quantidade',
            field=models.IntegerField(default=1),
        ),
    ]
