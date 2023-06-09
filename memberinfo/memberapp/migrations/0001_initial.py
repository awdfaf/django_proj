# Generated by Django 4.0.1 on 2023-01-30 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('mem_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('mem_pass', models.CharField(max_length=20)),
                ('mem_name', models.CharField(max_length=20)),
                ('mem_bir', models.DateTimeField(max_length=20)),
                ('mem_add1', models.CharField(max_length=60)),
                ('mem_add2', models.CharField(max_length=50)),
                ('mem_hp', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'member',
                'managed': False,
            },
        ),
    ]
