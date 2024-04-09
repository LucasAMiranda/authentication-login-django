# Generated by Django 5.0.4 on 2024-04-04 21:00

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0006_delete_mymodel_alter_usuarios_cpf"),
    ]

    operations = [
        migrations.CreateModel(
            name="MyModel",
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
                ("cpf", cpf_field.models.CPFField(max_length=14, verbose_name="cpf")),
            ],
        ),
        migrations.AlterField(
            model_name="usuarios",
            name="cpf",
            field=cpf_field.models.CPFField(
                max_length=14, primary_key=True, serialize=False
            ),
        ),
    ]