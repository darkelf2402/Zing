# Generated by Django 4.0.6 on 2022-08-02 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0016_rename_customerr_chatr_owner_chatr_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatr',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatr',
            name='owner',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]