# Generated by Django 4.2.7 on 2024-02-04 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_student_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Elligible', models.CharField(max_length=20)),
                ('bloodgroop', models.CharField(max_length=5)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
    ]
