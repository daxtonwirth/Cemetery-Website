# Generated by Django 4.1.5 on 2023-02-03 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_grave_birth_alter_grave_death'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grave',
            name='reference',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
