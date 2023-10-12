# Generated by Django 3.2.8 on 2023-09-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToppingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='pizzamodel',
            name='toppings',
            field=models.ManyToManyField(to='pizza.ToppingsModel', verbose_name='toppings'),
        ),
    ]