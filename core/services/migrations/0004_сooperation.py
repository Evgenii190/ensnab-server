# Generated by Django 4.0.6 on 2023-01-08 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_serviceslider_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Сooperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Сотрудничество',
                'verbose_name_plural': 'Сотрудничество',
            },
        ),
    ]
