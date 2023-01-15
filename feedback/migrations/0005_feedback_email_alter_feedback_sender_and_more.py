# Generated by Django 4.0.3 on 2022-05-07 19:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_alter_feedback_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='sender',
            field=models.CharField(max_length=150, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='subject',
            field=models.CharField(max_length=5000, verbose_name='Subject'),
        ),
    ]