# Generated by Django 5.0.2 on 2024-02-13 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_tenant_user_delete_tenancy_delete_tenant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='user',
        ),
        migrations.DeleteModel(
            name='Tenancy',
        ),
        migrations.DeleteModel(
            name='Tenant',
        ),
    ]
