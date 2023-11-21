# Generated by Django 4.2.7 on 2023-11-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2048)),
                ('plot', models.TextField()),
                ('rating', models.IntegerField()),
                ('release_date', models.DateField()),
            ],
        ),
    ]
