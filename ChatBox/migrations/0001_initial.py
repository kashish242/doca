# Generated by Django 2.1.1 on 2018-10-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suid', models.CharField(max_length=100)),
                ('ruid', models.CharField(max_length=100)),
                ('msg', models.CharField(max_length=100)),
                ('imgmsg', models.CharField(max_length=100)),
                ('docmsg', models.CharField(max_length=100)),
                ('msgtime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
