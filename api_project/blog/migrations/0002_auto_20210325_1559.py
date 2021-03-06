# Generated by Django 3.1.7 on 2021-03-25 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='blog_thumbnail/'),
        ),
    ]
