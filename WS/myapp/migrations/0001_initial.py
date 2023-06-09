# Generated by Django 4.1.7 on 2023-03-23 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Безымянный', max_length=100)),
                ('price', models.DecimalField(decimal_places=1, max_digits=100)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='WorkerJobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('login', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('worktitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workersjob', to='myapp.workerjobtitle')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chair', models.IntegerField(default=1)),
                ('ordertime', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(default='Занят', max_length=200)),
                ('position', models.IntegerField(default=1)),
                ('totalprice', models.DecimalField(decimal_places=1, max_digits=100)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workr', to='myapp.workers')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('finish', models.DateTimeField(auto_now_add=True)),
                ('orders', models.ManyToManyField(related_name='rdrs', to='myapp.order')),
                ('workers', models.ManyToManyField(related_name='workrws', to='myapp.workers')),
            ],
        ),
    ]
