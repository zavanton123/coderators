# Generated by Django 3.1.2 on 2020-11-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Published'),
        ),
    ]