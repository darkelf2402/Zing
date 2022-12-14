# Generated by Django 4.0.6 on 2022-08-02 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_rename_productt_chatr_chad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatr',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='chatr',
            old_name='chat_user',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='chatr',
            name='customer',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
