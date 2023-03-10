# Generated by Django 4.1.4 on 2022-12-30 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_rename_category_product_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductСharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('сharacteristic', models.CharField(max_length=64, verbose_name='Характеристика')),
                ('value', models.CharField(max_length=64, verbose_name='Название продукта')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product', to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
