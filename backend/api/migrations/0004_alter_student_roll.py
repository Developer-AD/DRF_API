# Generated by Django 5.0.4 on 2024-06-23 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_student_remove_profile_user_delete_myuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(null=True),
        ),
    ]
