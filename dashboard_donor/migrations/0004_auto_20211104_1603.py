# Generated by Django 3.2.7 on 2021-11-04 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard_donor', '0003_notifications_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('message', models.CharField(max_length=2000)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_donor_report', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='notifications',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_donor_notifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=2000)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard_donor.report')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_donor_response', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
