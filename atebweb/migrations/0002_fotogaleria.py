# Generated by Django 2.2.4 on 2019-11-26 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atebweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoGaleria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='gallery')),
            ],
            options={
                'verbose_name': 'Foto Para Galería',
                'verbose_name_plural': 'Fotos Para Galería',
            },
        ),
    ]
