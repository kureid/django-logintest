# Generated by Django 3.1.1 on 2020-09-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=5, null=True)),
                ('use', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
            ],
        ),
    ]
