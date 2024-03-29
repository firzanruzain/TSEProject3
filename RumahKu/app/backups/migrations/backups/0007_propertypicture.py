# Generated by Django 5.0.2 on 2024-02-13 01:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_owner_user_searcher_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='property_pictures/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='app.property')),
            ],
        ),
    ]
