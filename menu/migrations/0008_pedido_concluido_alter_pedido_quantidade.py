# Generated by Django 4.1.7 on 2024-06-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_alter_pedido_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='concluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='quantidade',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]