# Generated by Django 5.1.7 on 2025-03-18 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_animal'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='animals/')),
                ('is_primary', models.BooleanField(default=False)),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='animals.animal')),
            ],
        ),
    ]
