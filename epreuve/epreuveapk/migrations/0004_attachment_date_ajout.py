# Generated by Django 4.2.2 on 2023-06-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epreuveapk', '0003_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='date_ajout',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
