# Generated by Django 4.1.1 on 2022-10-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruits', models.CharField(max_length=255)),
                ('vegitable', models.CharField(max_length=255)),
            ],
        ),
    ]
