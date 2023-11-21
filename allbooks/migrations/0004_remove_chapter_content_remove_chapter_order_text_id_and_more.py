# Generated by Django 4.2.7 on 2023-11-14 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allbooks', '0003_collection_alter_book_genre_book_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='content',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='order',
        ),
        migrations.AddField(
            model_name='text',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allbooks.collection'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='text',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allbooks.chapter'),
        ),
    ]
