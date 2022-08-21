# Generated by Django 4.0.3 on 2022-08-21 02:55

import apps.editor_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor_app', '0006_item_position_alter_item_item_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='element_type',
            field=models.CharField(choices=[('canvas', 'canvas'), ('text', 'text'), ('image', 'image')], default=apps.editor_app.models.PositionTypes['CANVAS'], max_length=250, verbose_name='Element type'),
        ),
    ]