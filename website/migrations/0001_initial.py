# Generated by Django 4.1.5 on 2023-02-02 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('birth', models.CharField(blank=True, max_length=30, null=True)),
                ('death', models.CharField(blank=True, max_length=30, null=True)),
                ('veteran', models.BooleanField(blank=True, null=True)),
                ('headstone', models.BooleanField(blank=True, null=True)),
                ('reference', models.CharField(max_length=10)),
                ('Grid', models.IntegerField(blank=True, null=True)),
                ('Ward', models.IntegerField(blank=True, null=True)),
                ('Block', models.IntegerField(blank=True, null=True)),
                ('Lot', models.IntegerField(blank=True, null=True)),
                ('Plot', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]