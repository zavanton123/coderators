# Generated by Django 3.1.3 on 2021-01-01 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0003_auto_20210101_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='photos/<django.db.models.fields.CharField>/%Y/%m/%d', verbose_name='avatar'),
        ),
    ]