# Generated by Django 2.2.10 on 2020-10-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='score',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
    ]