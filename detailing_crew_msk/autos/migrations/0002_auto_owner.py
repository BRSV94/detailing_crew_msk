# Generated by Django 3.2.16 on 2024-12-12 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autos', '0001_initial'),
        ('detailing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autos', to='detailing.clientuser', verbose_name='Владелец авто'),
        ),
    ]
