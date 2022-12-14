# Generated by Django 4.1.3 on 2022-11-09 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='menu_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.FloatField()),
                ('spice', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('diet_id', models.IntegerField()),
            ],
        ),
    ]
