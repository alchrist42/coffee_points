# Generated by Django 3.2.4 on 2021-06-17 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0004_alter_order_volume'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',)},
        ),
    ]
