# Generated by Django 4.0.7 on 2023-01-03 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=10)),
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.CharField(max_length=140)),
                ('verified', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('validity', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
