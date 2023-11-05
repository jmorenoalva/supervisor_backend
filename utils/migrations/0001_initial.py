# Generated by Django 4.1.7 on 2023-11-04 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=7, unique=True, verbose_name='Periodo')),
                ('year', models.IntegerField(verbose_name='Año')),
                ('month', models.CharField(max_length=2, verbose_name='Mes')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Period',
                'verbose_name_plural': 'Periods',
                'ordering': ['period'],
            },
        ),
        migrations.CreateModel(
            name='TypeDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Codigo')),
                ('alias', models.CharField(max_length=10, verbose_name='Alias')),
                ('description', models.CharField(blank=True, max_length=254, verbose_name='Descripcion')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'TypeDocument',
                'verbose_name_plural': 'TypeDocuments',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='TypeInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Codigo')),
                ('description', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'TypeInvoice',
                'verbose_name_plural': 'TypesInvoices',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Ubigeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, unique=True, verbose_name='Codigo')),
                ('region', models.CharField(max_length=100, verbose_name='Departamento')),
                ('city', models.CharField(max_length=100, verbose_name='Provincia')),
                ('district', models.CharField(max_length=100, verbose_name='Distrito')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Ubigeo',
                'verbose_name_plural': 'Ubigeos',
                'ordering': ['code'],
            },
        ),
        migrations.AddIndex(
            model_name='ubigeo',
            index=models.Index(fields=['code'], name='utils_ubige_code_627cd2_idx'),
        ),
        migrations.AddIndex(
            model_name='ubigeo',
            index=models.Index(fields=['region'], name='utils_ubige_region_8e2ab3_idx'),
        ),
        migrations.AddIndex(
            model_name='ubigeo',
            index=models.Index(fields=['city'], name='utils_ubige_city_51cc49_idx'),
        ),
        migrations.AddIndex(
            model_name='ubigeo',
            index=models.Index(fields=['district'], name='utils_ubige_distric_0c7b86_idx'),
        ),
        migrations.AddIndex(
            model_name='typeinvoice',
            index=models.Index(fields=['code'], name='utils_typei_code_e65df9_idx'),
        ),
        migrations.AddIndex(
            model_name='typedocument',
            index=models.Index(fields=['code'], name='utils_typed_code_d0c773_idx'),
        ),
        migrations.AddIndex(
            model_name='typedocument',
            index=models.Index(fields=['description'], name='utils_typed_descrip_fe701e_idx'),
        ),
        migrations.AddIndex(
            model_name='period',
            index=models.Index(fields=['period'], name='utils_perio_period_f188f8_idx'),
        ),
    ]