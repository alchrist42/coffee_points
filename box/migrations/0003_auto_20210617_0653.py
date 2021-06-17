# Generated by Django 3.2.4 on 2021-06-17 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0002_rename_boxes_box'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeePoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('place', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('done', models.BooleanField(default=False)),
                ('volume', models.FloatField(choices=[('small', 0.2), ('medium', 0.3), ('large', 0.5)], default=0.2)),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='box.coffeetype')),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='box.coffeepoint')),
            ],
        ),
        migrations.DeleteModel(
            name='Box',
        ),
    ]