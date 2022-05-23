# Generated by Django 4.0.4 on 2022-04-28 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
        ('users', '0001_initial'),
        ('checkout', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unregisteredorderitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item_unregistereduser', to='users.unregistered_users'),
        ),
        migrations.AddField(
            model_name='unregisteredorder',
            name='items',
            field=models.ManyToManyField(related_name='unregister_OrderItem', to='checkout.unregisteredorderitem'),
        ),
        migrations.AddField(
            model_name='unregisteredorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_unregistereduser', to='users.unregistered_users'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='products.products_combinations'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='OrderItem', to='checkout.orderitem'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to=settings.AUTH_USER_MODEL),
        ),
    ]