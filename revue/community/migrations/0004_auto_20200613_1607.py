# Generated by Django 2.2.12 on 2020-06-13 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20200613_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='hits',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]