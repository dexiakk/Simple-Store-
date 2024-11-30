# Generated by Django 5.1.3 on 2024-11-29 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_orders_created_at_alter_shoe_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='on_sale',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='shoe',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
