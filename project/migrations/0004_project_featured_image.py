# Generated by Django 4.2.3 on 2023-08-21 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_tag_project_vote_ratio_project_vote_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]