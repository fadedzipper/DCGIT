# Generated by Django 2.2.6 on 2020-07-17 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarmdata',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='处理人'),
        ),
    ]
