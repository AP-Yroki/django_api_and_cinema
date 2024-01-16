# Generated by Django 5.0.1 on 2024-01-15 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('country_manufacturer', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Category',
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('size', models.IntegerField()),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.manufacturer')),
            ],
        ),
        migrations.DeleteModel(
            name='Meal',
        ),
    ]