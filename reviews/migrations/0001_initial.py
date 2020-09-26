# Generated by Django 3.1 on 2020-09-25 15:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=255, verbose_name='店名')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('text', models.TextField(blank=True, verbose_name='口コミテキスト')),
                ('start', models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], verbose_name='星の数')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('男', '男'), ('女', '女')], max_length=10, verbose_name='性別')),
            ],
        ),
    ]
