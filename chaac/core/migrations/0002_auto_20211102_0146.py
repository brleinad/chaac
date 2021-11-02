# Generated by Django 3.1.13 on 2021-11-02 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=9),
            preserve_default=False,
        ),
    ]
