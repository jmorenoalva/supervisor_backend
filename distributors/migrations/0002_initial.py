# Generated by Django 4.1.7 on 2023-11-04 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('utils', '0001_initial'),
        ('distributors', '0001_initial'),
        ('clients', '0002_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='promoter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.promoter'),
        ),
        migrations.AddField(
            model_name='sales',
            name='sites_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clients.sitesclient'),
        ),
        migrations.AddField(
            model_name='sales',
            name='type_invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='utils.typeinvoice'),
        ),
        migrations.AddField(
            model_name='sales',
            name='ubigeo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='utils.ubigeo'),
        ),
        migrations.AddField(
            model_name='productdistributor',
            name='distributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='distributors.distributor'),
        ),
        migrations.AddField(
            model_name='productdistributor',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product'),
        ),
        migrations.AddField(
            model_name='distributor',
            name='type_document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='utils.typedocument'),
        ),
        migrations.AddField(
            model_name='distributor',
            name='ubigeo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='utils.ubigeo'),
        ),
        migrations.AddIndex(
            model_name='sales',
            index=models.Index(fields=['distributor'], name='distributor_distrib_f434fa_idx'),
        ),
        migrations.AddIndex(
            model_name='sales',
            index=models.Index(fields=['date'], name='distributor_date_675a53_idx'),
        ),
        migrations.AddIndex(
            model_name='sales',
            index=models.Index(fields=['client'], name='distributor_client__d3b15d_idx'),
        ),
        migrations.AddIndex(
            model_name='sales',
            index=models.Index(fields=['code_client'], name='distributor_code_cl_3d7971_idx'),
        ),
        migrations.AddIndex(
            model_name='sales',
            index=models.Index(fields=['district'], name='distributor_distric_4b613f_idx'),
        ),
        migrations.AddIndex(
            model_name='sales',
            index=models.Index(fields=['sites_client'], name='distributor_sites_c_c40aee_idx'),
        ),
        migrations.AddIndex(
            model_name='sales',
            index=models.Index(fields=['ubigeo'], name='distributor_ubigeo__84450f_idx'),
        ),
        migrations.AddIndex(
            model_name='sales',
            index=models.Index(fields=['product'], name='distributor_product_e1f310_idx'),
        ),
        migrations.AddIndex(
            model_name='sales',
            index=models.Index(fields=['code_product'], name='distributor_code_pr_3f38df_idx'),
        ),
        migrations.AddIndex(
            model_name='sales',
            index=models.Index(fields=['promoter'], name='distributor_promote_e0ac12_idx'),
        ),
        migrations.AddIndex(
            model_name='sales',
            index=models.Index(fields=['period'], name='distributor_period__019537_idx'),
        ),
        migrations.AddIndex(
            model_name='productdistributor',
            index=models.Index(fields=['code'], name='distributor_code_b5f4ee_idx'),
        ),
        migrations.AddIndex(
            model_name='productdistributor',
            index=models.Index(fields=['distributor'], name='distributor_distrib_b6abdd_idx'),
        ),
        migrations.AddIndex(
            model_name='productdistributor',
            index=models.Index(fields=['product'], name='distributor_product_b02b87_idx'),
        ),
        migrations.AddIndex(
            model_name='distributor',
            index=models.Index(fields=['code'], name='distributor_code_46ad74_idx'),
        ),
    ]