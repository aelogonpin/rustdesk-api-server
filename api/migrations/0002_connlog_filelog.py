# Generated by Django 5.0.3 on 2024-04-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=20, null=True, verbose_name='Action')),
                ('conn_id', models.CharField(max_length=10, null=True, verbose_name='Connection ID')),
                ('from_ip', models.CharField(max_length=30, null=True, verbose_name='From IP')),
                ('from_id', models.CharField(max_length=20, null=True, verbose_name='From ID')),
                ('rid', models.CharField(max_length=20, null=True, verbose_name='To ID')),
                ('conn_start', models.DateTimeField(null=True, verbose_name='Connected')),
                ('conn_end', models.DateTimeField(null=True, verbose_name='Disconnected')),
                ('session_id', models.CharField(max_length=60, null=True, verbose_name='Session ID')),
                ('uuid', models.CharField(max_length=60, null=True, verbose_name='uuid')),
            ],
        ),
        migrations.CreateModel(
            name='FileLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=500, verbose_name='Path')),
                ('remote_id', models.CharField(default='0', max_length=20, verbose_name='Remote ID')),
                ('user_id', models.CharField(default='0', max_length=20, verbose_name='User ID')),
                ('user_ip', models.CharField(default='0', max_length=20, verbose_name='User IP')),
                ('filesize', models.CharField(default='', max_length=500, verbose_name='Filesize')),
                ('direction', models.IntegerField(default=0, verbose_name='Direction')),
                ('logged_at', models.DateTimeField(null=True, verbose_name='Logged At')),
            ],
        ),
    ]
