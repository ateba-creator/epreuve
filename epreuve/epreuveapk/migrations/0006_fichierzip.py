# Generated by Django 4.2.2 on 2023-06-14 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epreuveapk', '0005_image_delete_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fichierzip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='zipfile')),
                ('nom_doc', models.CharField(max_length=50)),
            ],
        ),
    ]
