# Generated by Django 2.2.1 on 2019-05-24 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('card', models.PositiveIntegerField(default=0)),
                ('prev_card', models.PositiveIntegerField(default=0)),
                ('chip', models.PositiveIntegerField(default=0)),
                ('bet', models.PositiveIntegerField(default=0)),
                ('is_joined', models.BooleanField(default=False)),
                ('is_my_turn', models.BooleanField(default=False)),
                ('is_show_result', models.PositiveIntegerField(default=0)),
                ('last_approach', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('is_playing', models.BooleanField(default=False)),
                ('current_player_number', models.PositiveIntegerField(default=0)),
                ('stack', models.PositiveIntegerField(default=0)),
                ('join_players', models.ManyToManyField(null=True, to='network.Player')),
            ],
        ),
    ]