# Generated by Django 4.0.3 on 2022-08-21 01:59

import apps.editor_app.models
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('editor_app', '0003_alter_element_id_alter_elementtemplate_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='Active editing')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('styles', models.JSONField(verbose_name='Styles')),
                ('element_type', models.IntegerField(choices=[('canvas', 'canvas'), ('text', 'text'), ('image', 'image')], default=apps.editor_app.models.PositionTypes['CANVAS'], max_length=250, verbose_name='')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Item list',
            },
        ),
        migrations.RemoveField(
            model_name='elementtemplate',
            name='element',
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'List of projects'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='main_frame',
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Title'),
        ),
        migrations.DeleteModel(
            name='Element',
        ),
        migrations.DeleteModel(
            name='ElementTemplate',
        ),
        migrations.AddField(
            model_name='item',
            name='item_list',
            field=models.ManyToManyField(to='editor_app.project', verbose_name='Item list'),
        ),
        migrations.AddField(
            model_name='item',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='editor_app.item'),
        ),
        migrations.AddField(
            model_name='project',
            name='root_canvas',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='editor_app.item', verbose_name='Root canvas'),
        ),
    ]