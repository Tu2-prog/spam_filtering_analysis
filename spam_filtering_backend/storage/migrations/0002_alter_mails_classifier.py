# Generated by Django 4.2.7 on 2023-12-18 23:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("storage", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mails",
            name="classifier",
            field=models.IntegerField(),
        ),
    ]
