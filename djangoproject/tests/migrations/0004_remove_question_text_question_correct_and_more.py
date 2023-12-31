# Generated by Django 4.2.3 on 2023-07-23 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_alter_poll_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.AddField(
            model_name='question',
            name='correct',
            field=models.CharField(default='correct', max_length=256),
        ),
        migrations.AddField(
            model_name='question',
            name='option_one',
            field=models.CharField(default='var', max_length=256),
        ),
        migrations.AddField(
            model_name='question',
            name='option_three',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='question',
            name='option_two',
            field=models.CharField(default='var', max_length=256),
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.CharField(default='question', max_length=256),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
