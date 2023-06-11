# Generated by Django 4.2 on 2023-06-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiero_otro_mundo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='user',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dirección',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='user',
            name='telefono',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
