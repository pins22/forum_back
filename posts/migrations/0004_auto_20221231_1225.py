# Generated by Django 3.2.16 on 2022-12-31 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20221228_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='title',
            field=models.CharField(default=1, max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reply',
            name='last_changed',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
