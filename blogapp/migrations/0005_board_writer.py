# Generated by Django 2.0.13 on 2021-02-09 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20210209_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='writer',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
