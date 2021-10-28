# Generated by Django 3.2.7 on 2021-10-25 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Notifications",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("message", models.CharField(max_length=1000)),
                ("timestamp", models.DateTimeField(default=datetime.date.today)),
                ("status", models.CharField(max_length=20)),
            ],
        ),
    ]
