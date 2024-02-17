# Generated by Django 4.2.5 on 2024-02-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_category_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgrounFigure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=60)),
                ('title_2', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='background/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='Home.category'),
        ),
    ]