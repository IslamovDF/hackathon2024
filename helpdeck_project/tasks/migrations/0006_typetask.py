# Generated by Django 5.1.3 on 2024-11-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_task_contractor'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
    ]
