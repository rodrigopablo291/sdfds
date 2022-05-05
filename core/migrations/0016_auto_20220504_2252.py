# Generated by Django 3.2.13 on 2022-05-05 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_usuariopreferencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='idtipousuario',
        ),
        migrations.RemoveField(
            model_name='usuariopreferencia',
            name='preferencia',
        ),
        migrations.RemoveField(
            model_name='usuariopreferencia',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='usuarioproductoempresatitular',
            name='idproductoempresatitular',
        ),
        migrations.RemoveField(
            model_name='usuarioproductoempresatitular',
            name='idusuario',
        ),
        migrations.DeleteModel(
            name='PreferenciaPersonal',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='UsuarioPreferencia',
        ),
        migrations.DeleteModel(
            name='UsuarioProductoEmpresaTitular',
        ),
    ]