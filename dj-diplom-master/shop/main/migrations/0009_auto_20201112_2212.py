# Generated by Django 2.2.10 on 2020-11-12 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201112_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Product'),
        ),
    ]
