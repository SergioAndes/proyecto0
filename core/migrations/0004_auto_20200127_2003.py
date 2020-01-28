# Generated by Django 2.2.4 on 2020-01-28 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200127_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='direccion',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fechaFin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fechaInicio',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='lugar',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='presencial',
            field=models.BooleanField(default=False, null=True),
        ),
    ]