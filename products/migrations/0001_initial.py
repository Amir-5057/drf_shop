# Generated by Django 5.0.4 on 2024-04-12 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Characteristic',
                'verbose_name_plural': 'Characteristics',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='full name')),
                ('status', models.CharField(choices=[('New', 'new'), ('Accepted', 'accepted'), ('Progress', 'progress'), ('Cancelled', 'cancelled'), ('finished', 'finished')], default='New', max_length=20, verbose_name='status')),
                ('total_price', models.FloatField(default=0, verbose_name='total price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='CharacteristicValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('characteristic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='products.characteristic')),
            ],
            options={
                'verbose_name': 'characteristic value',
                'verbose_name_plural': 'characteristic values',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('discount', models.IntegerField(default=0, verbose_name='discount')),
                ('price', models.IntegerField(verbose_name='price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('short_desc', models.TextField(verbose_name='short description')),
                ('view_count', models.IntegerField(default=0, verbose_name='view count')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('desc', models.TextField(verbose_name='description')),
                ('left_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructions_left_image', to='media.media', verbose_name='left image')),
                ('right_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructions_right_image', to='media.media', verbose_name='right image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructions', to='products.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'instruction',
                'verbose_name_plural': 'instructions',
            },
        ),
        migrations.AddField(
            model_name='characteristic',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characteristics', to='products.product', verbose_name='product'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.media', verbose_name='image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='products.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'product image',
                'verbose_name_plural': 'product images',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.order', verbose_name='order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'order item',
                'verbose_name_plural': 'order items',
                'unique_together': {('order', 'product')},
            },
        ),
    ]
