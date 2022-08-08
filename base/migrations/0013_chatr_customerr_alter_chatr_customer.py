# Generated by Django 4.0.6 on 2022-08-02 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0012_alter_chatr_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatr',
            name='customerr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatr',
            name='customer',
            field=models.TextField(),
        ),
    ]
