# Generated by Django 4.0.4 on 2022-06-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OlonijayeSamsonTobi', models.CharField(max_length=200)),
                ('Psalmsage', models.CharField(max_length=200)),
                ('Created_date', models.DateTimeField(verbose_name='17/6-6:18')),
                ('Published_date', models.DateTimeField(verbose_name='17/6-6:18')),
            ],
        ),
    ]
