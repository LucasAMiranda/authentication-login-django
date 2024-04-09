# Generated by Django 5.0.4 on 2024-04-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuarios",
            fields=[
                (
                    "user_id_aluno_model",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("user_nome_aluno", models.CharField(max_length=150, null=True)),
                ("user_cpf", models.CharField(max_length=150, null=True)),
                ("user_escola", models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
