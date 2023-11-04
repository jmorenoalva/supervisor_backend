# Generated by Django 4.1.7 on 2023-11-04 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Codigo')),
                ('description', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('status', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'ActiveIngredient',
                'verbose_name_plural': 'ActiveIngredients',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Codigo')),
                ('description', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('status', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Presentation',
                'verbose_name_plural': 'Presentations',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Codigo')),
                ('description', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('resolution', models.CharField(max_length=255, verbose_name='Resolution')),
                ('indication', models.CharField(max_length=255, verbose_name='Indication')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['code', 'unit'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Codigo')),
                ('description', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('status', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
                'ordering': ['code'],
            },
        ),
        migrations.AddIndex(
            model_name='unit',
            index=models.Index(fields=['code'], name='product_uni_code_8f0dfd_idx'),
        ),
        migrations.AddField(
            model_name='product',
            name='active_ingredient',
            field=models.ManyToManyField(to='product.activeingredient'),
        ),
        migrations.AddField(
            model_name='product',
            name='presentation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.presentation'),
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.unit'),
        ),
        migrations.AddIndex(
            model_name='presentation',
            index=models.Index(fields=['code'], name='product_pre_code_302996_idx'),
        ),
        migrations.AddIndex(
            model_name='activeingredient',
            index=models.Index(fields=['code'], name='product_act_code_44ca55_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['code'], name='product_pro_code_f66008_idx'),
        ),
    ]
