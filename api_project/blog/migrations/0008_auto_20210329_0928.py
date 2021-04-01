# Generated by Django 3.1.7 on 2021-03-29 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210327_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='images',
            field=models.ManyToManyField(related_name='blog_comment_images', through='blog.BlogCommentImage', to='blog.Blog'),
        ),
        migrations.AddField(
            model_name='blogcommentimage',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blog'),
        ),
        migrations.AlterField(
            model_name='blogcommentimage',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogcomment'),
        ),
    ]
