# Generated by Django 2.2.12 on 2020-06-11 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='community.Review'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recomment',
            name='comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='community.Comment'),
            preserve_default=False,
        ),
    ]