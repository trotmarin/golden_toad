# Generated by Django 3.1.4 on 2020-12-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testtable',
            old_name='contect',
            new_name='add_pri',
        ),
        migrations.RenameField(
            model_name='testtable',
            old_name='title',
            new_name='add_sec',
        ),
        migrations.AddField(
            model_name='testtable',
            name='address',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testtable',
            name='apt_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testtable',
            name='city',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
