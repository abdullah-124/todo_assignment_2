# Generated by Django 5.0.1 on 2024-03-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_taksmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taksmodel',
            name='is_completed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
