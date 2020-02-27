# Generated by Django 2.2.6 on 2020-02-02 01:02


import ctf.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('PROGRAMMING', 'Programming'), ('CRYPTOGRAPHY', 'Cryptography'), ('PACKETANALYSIS', 'Packet Analysis'), ('TRIVIA', 'Trivia'), ('WEBAPP', 'Web App'), ('DATABASE', 'Database'), ('SYSADMIN', 'SysAdmin'), ('STEGANOGRAPHY', 'Steganography'), ('REVERSING', 'Reversing'), ('LOCKPICKING', 'Lockpicking'), ('FORENSICS', 'Forensics')], max_length=30)),
                ('link', models.URLField(blank=True, default='')),
                ('file', models.FileField(blank=True, upload_to='uploads/')),
                ('active', models.BooleanField(default=True)),
                ('dynamic_link', models.BooleanField(blank=True, default=False)),
            ],
            options={
                'ordering': ('category', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('stop_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('flag', models.CharField(max_length=50)),
                ('points', models.IntegerField()),
                ('hint', models.TextField()),
                ('penalty', models.IntegerField()),
                ('solved', models.IntegerField(default=0)),
                ('last_solved', models.DateTimeField(blank=True, null=True)),
                ('challenge', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='flags', to='ctf.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('logo', models.FileField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('active', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=0)),
                ('score_last', models.DateTimeField(default=django.utils.timezone.now)),
                ('secret', models.CharField(default=ctf.models.Team.create_secret, max_length=30)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='ctf.Contest')),
                ('hints', models.ManyToManyField(blank=True, related_name='hints', to='ctf.Flag')),
                ('members', models.ManyToManyField(blank=True, related_name='teams', to=settings.AUTH_USER_MODEL)),
                ('solved', models.ManyToManyField(blank=True, related_name='solvers', to='ctf.Flag')),
            ],
            options={
                'ordering': ('-score', 'score_last'),
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('correct', models.BooleanField(default=False)),
                ('guess', models.CharField(default='', max_length=128)),
                ('hinted', models.BooleanField(default=False)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='ctf.Challenge')),
                ('flag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='ctf.Flag')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='ctf.Team')),
            ],
            options={
                'ordering': ('time',),
            },
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier', models.CharField(choices=[('TITLE', 'Title Sponsor'), ('GOLD', 'Gold Sponsor'), ('SILVER', 'Silver Sponsor'), ('BRONZE', 'Bronze Sponsor')], max_length=20)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.Contest')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.Sponsor')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contest',
            name='sponsors',
            field=models.ManyToManyField(blank=True, through='ctf.Sponsorship', to='ctf.Sponsor'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenges', to='ctf.Contest'),
        ),
    ]
