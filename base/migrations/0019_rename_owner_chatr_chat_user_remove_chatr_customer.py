# Generated by Django 4.0.6 on 2022-08-02 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_chatr_customer_alter_chatr_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatr',
            old_name='owner',
            new_name='chat_user',
        ),
        migrations.RemoveField(
            model_name='chatr',
            name='customer',
        ),
    ]
