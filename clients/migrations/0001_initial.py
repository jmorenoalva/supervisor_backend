# Generated by Django 4.1.7 on 2023-11-04 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Codigo')),
                ('nro_document', models.CharField(max_length=20, unique=True, verbose_name='Codigo')),
                ('company_name', models.CharField(max_length=255, verbose_name='Razon_Social')),
                ('fiscal_address', models.CharField(max_length=255, verbose_name='Domicilio_Fiscal')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField(verbose_name='Item')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('phone', models.CharField(max_length=255, verbose_name='Telefono')),
                ('email', models.CharField(max_length=255, verbose_name='Correo')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ['sites_client', 'item'],
            },
        ),
        migrations.CreateModel(
            name='SitesClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, verbose_name='Codigo')),
                ('commercial_name', models.CharField(max_length=255, verbose_name='Nombre_Comercial')),
                ('address', models.CharField(max_length=255, verbose_name='Direccion')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Sites_client',
                'verbose_name_plural': 'Sites_clients',
                'ordering': ['client', 'code'],
            },
        ),
        migrations.CreateModel(
            name='TypeClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, unique=True, verbose_name='Codigo')),
                ('description', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Type_client',
                'verbose_name_plural': 'Type_clients',
                'ordering': ['code'],
            },
        ),
        migrations.AddIndex(
            model_name='typeclient',
            index=models.Index(fields=['code'], name='clients_typ_code_6eb203_idx'),
        ),
        migrations.AddField(
            model_name='sitesclient',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clients.client'),
        ),
    ]
