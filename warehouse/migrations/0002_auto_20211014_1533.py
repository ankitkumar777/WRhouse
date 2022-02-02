# Generated by Django 3.2.7 on 2021-10-14 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delievered_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.customer'),
        ),
        migrations.AlterField(
            model_name='stockrequest',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.supplier'),
        ),
    ]