# Generated by Django 4.0.6 on 2022-07-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=30, null=True)),
                ('full_name', models.CharField(max_length=30, null=True)),
                ('email_id', models.CharField(max_length=30, null=True)),
                ('contact1', models.CharField(max_length=30, null=True)),
                ('contact2', models.CharField(max_length=30, null=True)),
                ('total_days', models.CharField(max_length=30, null=True)),
                ('price', models.CharField(max_length=30, null=True)),
                ('dob', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='room_no',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]