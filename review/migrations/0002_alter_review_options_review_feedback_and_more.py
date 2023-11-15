# Generated by Django 4.1 on 2022-08-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Review'},
        ),
        migrations.AddField(
            model_name='review',
            name='feedback',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='user_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
