# Generated by Django 5.1.3 on 2024-11-21 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_shoe_gender_alter_shoe_shoe_high_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='gender',
            field=models.CharField(choices=[('female', 'Damskie'), ('unisex', 'Uniseks'), ('male', 'Męskie')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='preferedGender',
            field=models.CharField(choices=[('female', 'Damskie'), ('unisex', 'Uniseks'), ('male', 'Męskie')], max_length=50),
        ),
    ]