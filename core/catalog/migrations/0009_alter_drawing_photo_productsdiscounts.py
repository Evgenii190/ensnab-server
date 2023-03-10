# Generated by Django 4.0.6 on 2023-01-04 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_drawing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawing',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Чертеж'),
        ),
        migrations.CreateModel(
            name='ProductsDiscounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64, verbose_name='Описание скидки')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='discount', to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Скидка для продукта',
                'verbose_name_plural': 'Скидка для продуктов',
            },
        ),
    ]
