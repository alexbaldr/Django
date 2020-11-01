# Generated by Django 2.2.10 on 2020-11-01 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_review_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='score',
        ),
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to=settings.AUTH_USER_MODEL, verbose_name='Имя'),
        ),
    ]
