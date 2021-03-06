# Generated by Django 4.0.3 on 2022-04-02 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('address', models.CharField(max_length=255, unique=True)),
                ('image', models.CharField(blank=True, max_length=255)),
                ('map', models.CharField(blank=True, max_length=255)),
                ('listed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.CharField(blank=True, max_length=255)),
                ('listed', models.BooleanField(default=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campus.campus')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.CharField(blank=True, max_length=255)),
                ('listed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher')], default='S', max_length=1)),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campus.campus')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('listed', models.BooleanField(default=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campus.menucategory')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.CharField(blank=True, max_length=255)),
                ('listed', models.BooleanField(default=True)),
                ('event_start', models.DateTimeField()),
                ('event_end', models.DateTimeField()),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campus.campus')),
            ],
        ),
        migrations.AddField(
            model_name='campus',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campus.region'),
        ),
    ]
