# Generated by Django 2.1.1 on 2018-10-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login2', '0009_user_userapplied'),
    ]

    operations = [
        migrations.CreateModel(
            name='udp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(default='static/background.jpg', upload_to='static/')),
            ],
        ),
    ]
