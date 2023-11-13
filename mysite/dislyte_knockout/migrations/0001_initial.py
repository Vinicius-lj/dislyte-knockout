# Generated by Django 4.2.1 on 2023-07-27 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Esper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('classe', models.CharField(max_length=50)),
                ('rarity', models.CharField(max_length=50)),
                ('leader_effect', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('server', models.CharField(max_length=50)),
                ('guild', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Player_esper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ressonance', models.IntegerField(default=0)),
                ('team', models.IntegerField(default=1)),
                ('ifleader', models.BooleanField(default=False)),
                ('esper_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dislyte_knockout.esper')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dislyte_knockout.player')),
            ],
        ),
    ]