# Generated by Django 5.0.4 on 2024-04-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_book_isbn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('book', models.ManyToManyField(to='catalog.book')),
            ],
        ),
    ]
