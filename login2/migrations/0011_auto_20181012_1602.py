# Generated by Django 2.1.1 on 2018-10-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login2', '0010_udp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='udp',
        ),
        migrations.AddField(
            model_name='user',
            name='dp',
            field=models.CharField(default='uploads/A@DOCA@IIIT@DPdefualt.png', max_length=100),
        ),
    ]
