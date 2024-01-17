# Generated by Django 5.0 on 2024-01-11 08:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('borrowing_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Books/media/uploads/')),
                ('category', models.ManyToManyField(to='categories.category')),
            ],
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField(max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='reviews',
            field=models.ManyToManyField(through='Books.BookReview', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BorrowingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowing_date', models.DateTimeField(auto_now_add=True)),
                ('returned_date', models.DateTimeField(blank=True, null=True)),
                ('returned_amount', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
