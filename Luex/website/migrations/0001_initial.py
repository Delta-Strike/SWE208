# Generated by Django 4.1.13 on 2024-06-23 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('name', models.CharField(default='Clothes', max_length=250)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('description', models.TextField(default='No description')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X Large'), ('2XL', '2X Large')], default='Size not available', max_length=50)),
                ('not_available', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('stock', models.PositiveIntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default='Category not available', on_delete=django.db.models.deletion.CASCADE, to='website.category')),
            ],
        ),
    ]
