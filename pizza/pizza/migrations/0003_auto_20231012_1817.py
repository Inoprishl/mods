# Generated by Django 3.2.8 on 2023-10-12 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_auto_20230907_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pizza.pizzamodel_toppings',),
        ),
        migrations.AlterModelOptions(
            name='pizzamodel',
            options={'verbose_name': 'My pizza resipes(vn)', 'verbose_name_plural': 'Pizza resipes(vnp)'},
        ),
        migrations.AlterModelOptions(
            name='toppingsmodel',
            options={'verbose_name': 'Toppings(vn)', 'verbose_name_plural': 'Toppings(vnp)'},
        ),
    ]