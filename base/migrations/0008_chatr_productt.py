# Generated by Django 4.0.6 on 2022-08-01 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_productd_body_chatr'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatr',
            name='productt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.productd'),
        ),
    ]