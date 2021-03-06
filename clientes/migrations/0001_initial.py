# Generated by Django 2.1 on 2018-08-03 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('age', models.IntegerField()),
                ('salaray', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bio', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='clients_photos')),
            ],
        ),
    ]
