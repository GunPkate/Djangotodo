# Generated by Django 3.1 on 2021-08-16 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Projectt',
        ),
    ]
