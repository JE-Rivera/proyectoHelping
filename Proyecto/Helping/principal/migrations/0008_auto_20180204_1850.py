# Generated by Django 2.0.2 on 2018-02-05 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_facultad_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_carrera', models.CharField(max_length=80)),
                ('cantidad_materias', models.PositiveIntegerField(verbose_name='Cantidad de materias')),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
                'ordering': ['universidad'],
            },
        ),
        migrations.AlterModelOptions(
            name='facultad',
            options={'ordering': ['nombre_facultad'], 'verbose_name': 'Facultad', 'verbose_name_plural': 'Facultades'},
        ),
        migrations.AddField(
            model_name='carrera',
            name='facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Facultad'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='universidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Universidad'),
        ),
    ]
