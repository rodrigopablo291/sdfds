# Generated by Django 3.2.13 on 2022-05-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombretipousuario', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo Usuario',
                'verbose_name_plural': 'Tipo Usuario',
            },
        ),
    ]
