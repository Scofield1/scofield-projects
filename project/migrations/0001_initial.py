# Generated by Django 3.1.2 on 2021-12-10 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField(max_length=11)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
