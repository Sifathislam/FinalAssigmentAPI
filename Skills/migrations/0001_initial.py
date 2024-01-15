# Generated by Django 4.2.7 on 2024-01-15 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_pdf', models.FileField(upload_to='Skills/resumes/')),
            ],
        ),
        migrations.CreateModel(
            name='SkillsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_skill', models.ImageField(upload_to='Skills/media/images')),
                ('Prficiency_levels', models.CharField(choices=[('➊', 1), ('➊ ➋', 2), ('➊ ➋ ➌', 3), ('➊ ➋ ➌ ➍', 4), ('➊ ➋ ➌ ➍ ➎', 5)], max_length=50)),
            ],
        ),
    ]