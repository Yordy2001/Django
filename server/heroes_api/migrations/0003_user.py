# Generated by Django 4.0.4 on 2022-05-15 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes_api', '0002_alter_power_stats_combat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=100)),
                ('permission', models.CharField(max_length=70)),
            ],
        ),
    ]
