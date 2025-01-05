# Generated by Django 5.1.4 on 2025-01-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0002_rename_discipline_activity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='discipline',
            new_name='activity',
        ),
        migrations.AlterField(
            model_name='workout',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
    ]
