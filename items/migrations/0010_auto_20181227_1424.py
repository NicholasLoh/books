# Generated by Django 2.1.3 on 2018-12-27 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20181217_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='stream',
            field=models.CharField(choices=[('all', '全部'), ('理科', '理科'), ('文商', '文商科'), ('商', '商科'), ('商文商', '商文商')], max_length=100),
        ),
    ]
