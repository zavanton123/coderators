# Generated by Django 3.1.3 on 2021-01-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]