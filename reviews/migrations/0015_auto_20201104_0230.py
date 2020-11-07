# Generated by Django 3.1 on 2020-11-03 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_auto_20201102_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='review',
            name='image1',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='画像URL1'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image2',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='画像URL2'),
        ),
        migrations.AlterField(
            model_name='review',
            name='max_number',
            field=models.IntegerField(default=30, verbose_name='定員'),
        ),
        migrations.AlterField(
            model_name='review',
            name='store_price',
            field=models.IntegerField(default=3000, verbose_name='設定価格'),
        ),
    ]
