# Generated by Django 4.1 on 2022-08-21 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0005_recipe_ingredients"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="image",
            field=models.ImageField(
                null=True, upload_to="recipes-images/", verbose_name="image"
            ),
        ),
    ]
