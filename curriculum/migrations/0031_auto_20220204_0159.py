# Generated by Django 3.2 on 2022-02-04 01:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0030_auto_20210511_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslots',
            name='standard',
        ),
        migrations.RemoveField(
            model_name='workingdays',
            name='standard',
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=ckeditor.fields.RichTextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_body',
            field=ckeditor.fields.RichTextField(max_length=500),
        ),
        migrations.DeleteModel(
            name='SlotSubject',
        ),
        migrations.DeleteModel(
            name='TimeSlots',
        ),
        migrations.DeleteModel(
            name='WorkingDays',
        ),
    ]
