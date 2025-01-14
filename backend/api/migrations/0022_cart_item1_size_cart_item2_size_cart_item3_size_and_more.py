# Generated by Django 5.1.3 on 2024-11-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_shoe_gender_alter_userdetails_preferedgender'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='item1_size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='item2_size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='item3_size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='item4_size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='gender',
            field=models.CharField(choices=[('unisex', 'Uniseks'), ('female', 'Damskie'), ('male', 'Męskie')], max_length=50),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='shoe_high',
            field=models.CharField(choices=[('high', 'High Top'), ('mid', 'Mid Top'), ('low', 'Low Top')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='preferedGender',
            field=models.CharField(choices=[('unisex', 'Uniseks'), ('female', 'Damskie'), ('male', 'Męskie')], max_length=50),
        ),
    ]
