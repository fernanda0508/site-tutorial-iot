# Generated by Django 4.2.4 on 2023-09-16 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0004_alter_card_imagem_card_alter_card_imagem_conteudo'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='conteudo',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='card',
            name='descricao',
            field=models.CharField(max_length=300),
        ),
    ]
