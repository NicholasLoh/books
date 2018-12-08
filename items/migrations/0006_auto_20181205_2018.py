# Generated by Django 2.1.3 on 2018-12-05 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181205_1104'),
        ('items', '0005_auto_20181205_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='picture',
            field=models.ManyToManyField(to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='item',
            name='stream',
            field=models.CharField(choices=[('all', '全部'), ('S', '理科'), ('AC', '文商科'), ('C', '商科')], max_length=4),
        ),
    ]
