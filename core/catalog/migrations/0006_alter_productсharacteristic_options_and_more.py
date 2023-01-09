# Generated by Django 4.1.4 on 2022-12-30 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_productсharacteristic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productсharacteristic',
            options={'verbose_name': 'Характеристики для продуктов', 'verbose_name_plural': 'Характеристики для продуктов'},
        ),
        migrations.AlterField(
            model_name='productсharacteristic',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='characteristics', to='catalog.product', verbose_name='Продукт'),
        ),
    ]
