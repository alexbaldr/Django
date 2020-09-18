# Generated by Django 2.2.10 on 2020-09-04 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('ram', models.IntegerField()),
                ('pixel', models.IntegerField()),
                ('duble_camera', models.BooleanField(null=True)),
                ('processor', models.CharField(max_length=50)),
                ('screen', models.CharField(max_length=50)),
                ('fm', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Xiomi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.CharField(max_length=200)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Sumsung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.CharField(max_length=200)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Iphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.CharField(max_length=200)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
    ]