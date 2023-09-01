# Generated by Django 4.2.4 on 2023-08-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Evenement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("pdf", models.FileField(upload_to="evenements/pdfs/")),
                ("photo", models.ImageField(upload_to="evenements/photos/")),
                ("date_debut", models.DateTimeField()),
                ("date_fin", models.DateTimeField()),
            ],
        ),
    ]