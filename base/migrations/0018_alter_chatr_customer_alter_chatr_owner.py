# Generated by Django 4.0.6 on 2022-08-02 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0017_alter_chatr_customer_alter_chatr_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatr',
            name='customer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='chatr',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
