# Generated by Django 4.2.1 on 2023-08-08 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dislyte_knockout', '0003_alter_player_esper_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player_esper',
            name='version',
            field=models.CharField(default=0, max_length=15),
        ),
    ]