# Generated by Django 4.1.7 on 2023-03-23 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='change',
            options={'verbose_name': 'Смена', 'verbose_name_plural': 'Смены'},
        ),
        migrations.AlterModelOptions(
            name='workerjobtitle',
            options={'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AlterModelOptions(
            name='workers',
            options={'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
    ]
