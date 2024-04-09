# Generated by Django 5.0.4 on 2024-04-04 00:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usuarios",
            old_name="user_escola",
            new_name="escola",
        ),
        migrations.RenameField(
            model_name="usuarios",
            old_name="user_id_aluno_model",
            new_name="id_aluno_model",
        ),
        migrations.RenameField(
            model_name="usuarios",
            old_name="user_cpf",
            new_name="nome_aluno",
        ),
        migrations.RemoveField(
            model_name="usuarios",
            name="user_nome_aluno",
        ),
        migrations.AddField(
            model_name="usuarios",
            name="cpf",
            field=models.IntegerField(max_length=11, null=True),
        ),
    ]