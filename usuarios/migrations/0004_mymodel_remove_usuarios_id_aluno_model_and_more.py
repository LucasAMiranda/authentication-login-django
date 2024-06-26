# Generated by Django 5.0.4 on 2024-04-04 19:57

import cpf_field.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0003_usuarios_turma"),
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
        migrations.RemoveField(
            model_name="usuarios",
            name="id_aluno_model",
        ),
        migrations.AlterField(
            model_name="usuarios",
            name="cpf",
            field=models.IntegerField(
                default=1, primary_key=True, serialize=False
            ),
            preserve_default=False,
        ),
    ]
