# Generated by Django 4.0.1 on 2023-01-27 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lprod',
            fields=[
                ('lprod_id', models.IntegerField(max_length=20)),
                ('lprod_gu', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('lprod_nm', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'lprod',
                'managed': False,
            },
        ),
    ]
