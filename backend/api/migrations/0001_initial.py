# Generated by Django 5.1.3 on 2024-11-14 15:52

import api.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Manufacturers',
            },
        ),
        migrations.CreateModel(
            name='ShoeCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'ShoeCategories',
            },
        ),
        migrations.CreateModel(
            name='ShoeCollections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'ShoeCollections',
            },
        ),
        migrations.CreateModel(
            name='ShoeColors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=7)),
            ],
            options={
                'verbose_name_plural': 'ShoesColors',
            },
        ),
        migrations.CreateModel(
            name='ShoeSizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'ShoeSizes',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(default='Shoe Description')),
                ('bestseller', models.BooleanField(blank=True)),
                ('gender', models.CharField(choices=[('unisex', 'Uniseks'), ('male', 'Męskie'), ('female', 'Damskie')], max_length=50)),
                ('shoe_high', models.CharField(choices=[('mid', 'Mid Top'), ('high', 'High Top'), ('low', 'Low Top')], max_length=50)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.manufacturers')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.shoecategories')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.shoecollections')),
                ('shoe_sizes', models.ManyToManyField(to='api.shoesizes')),
            ],
            options={
                'verbose_name_plural': 'Shoes',
            },
        ),
        migrations.CreateModel(
            name='ShoeImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(default='black', max_length=10)),
                ('image1', models.ImageField(null=True, upload_to=api.models.shoe_gallery_upload_to)),
                ('image2', models.ImageField(null=True, upload_to=api.models.shoe_gallery_upload_to)),
                ('image3', models.ImageField(null=True, upload_to=api.models.shoe_gallery_upload_to)),
                ('image4', models.ImageField(null=True, upload_to=api.models.shoe_gallery_upload_to)),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_gallery', to='api.shoe')),
            ],
            options={
                'verbose_name_plural': 'Shoe Images Gallery',
            },
        ),
        migrations.CreateModel(
            name='ShoeVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(default='images/mainImages/default_shoe.png', upload_to='images/shoes/main_images/')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.shoecolors')),
                ('images_gallery', models.ManyToManyField(to='api.shoeimagegallery')),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='api.shoe')),
            ],
            options={
                'verbose_name_plural': 'Shoe Variants',
            },
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('preferedGender', models.CharField(choices=[('unisex', 'Uniseks'), ('male', 'Męskie'), ('female', 'Damskie')], max_length=50)),
                ('dateOfBirth', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=api.models.avatar_upload_to)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userEmail', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UsersDetails',
            },
        ),
    ]