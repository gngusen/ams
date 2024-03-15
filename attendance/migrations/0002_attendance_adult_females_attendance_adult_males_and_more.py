# Generated by Django 5.0.2 on 2024-02-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='adult_females',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='adult_males',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='child_females',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='child_males',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='total_offerings',
            field=models.BigIntegerField(null=True),
        ),
    ]