# Generated by Django 3.2.4 on 2021-09-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_recipecard_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
