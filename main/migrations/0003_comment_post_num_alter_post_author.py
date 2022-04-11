# Generated by Django 4.0.3 on 2022-04-11 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_num',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='main.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_num', to=settings.AUTH_USER_MODEL),
        ),
    ]
