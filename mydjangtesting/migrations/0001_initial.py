# Generated by Django 3.0.5 on 2020-04-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formulaire_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champ_texte', models.CharField(max_length=400)),
                ('champ_email', models.EmailField(max_length=40)),
                ('champ_decimal', models.DecimalField(decimal_places=3, max_digits=4)),
                ('champ_date', models.DateField()),
                ('champ_heure', models.TimeField()),
            ],
        ),
    ]
