# Generated by Django 3.0.5 on 2020-05-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='imię')),
                ('last_name', models.CharField(max_length=100, verbose_name='nazwisko')),
                ('about', models.TextField(blank=True, verbose_name='o autorze')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='zdjęcie')),
            ],
            options={
                'verbose_name': 'autor',
                'verbose_name_plural': 'autorzy',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title'], 'verbose_name': 'książka', 'verbose_name_plural': 'książki'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AlterField(
            model_name='book',
            name='published_at',
            field=models.DateField(verbose_name='data publikacji'),
        ),
        migrations.AlterField(
            model_name='book',
            name='short_description',
            field=models.TextField(verbose_name='opis'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='tytuł'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books', to='books.Author', verbose_name='autorzy'),
        ),
    ]
