# Generated by Django 2.1.1 on 2019-12-19 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pessoa', '0065_auto_20191219_0536'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='gestor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gestor', to=settings.AUTH_USER_MODEL),
        ),
    ]
