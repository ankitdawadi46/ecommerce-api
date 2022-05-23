# Generated by Django 4.0.4 on 2022-04-28 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewproducts',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='products_stocks',
            name='products_combinations_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products_combinations'),
        ),
        migrations.AddField(
            model_name='products_combinations',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
        migrations.AddField(
            model_name='products',
            name='brand_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brand'),
        ),
        migrations.AddField(
            model_name='products',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categories'),
        ),
        migrations.AddField(
            model_name='products',
            name='subcategory_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.subcategories'),
        ),
        migrations.AddField(
            model_name='product_variations_options',
            name='product_variation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product_variations'),
        ),
        migrations.AddField(
            model_name='product_variations',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
        migrations.AddField(
            model_name='product_images',
            name='image_galleries_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.image_galleries'),
        ),
        migrations.AddField(
            model_name='product_images',
            name='product_variations_value_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products_combinations'),
        ),
        migrations.AddField(
            model_name='product_cache',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
        migrations.AddField(
            model_name='festiveseasonproducts',
            name='festive_season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.festiveseasons'),
        ),
        migrations.AddField(
            model_name='festiveseasonproducts',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
        migrations.AddField(
            model_name='commoncategories',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categories'),
        ),
        migrations.AddField(
            model_name='clientsessionwishlistmap',
            name='client_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.clientsession'),
        ),
        migrations.AddField(
            model_name='clientsessionwishlistmap',
            name='product_combinations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products_combinations'),
        ),
        migrations.AddField(
            model_name='clientsessionwishlistmap',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
        migrations.AddField(
            model_name='clientsessioncartmap',
            name='client_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.clientsession'),
        ),
        migrations.AddField(
            model_name='clientsessioncartmap',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products_combinations'),
        ),
        migrations.AddField(
            model_name='clientsession',
            name='logged_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='subcategories',
            unique_together={('subcategoryName', 'category_id')},
        ),
    ]