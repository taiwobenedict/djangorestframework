# Generated by Django 4.1.2 on 2022-10-06 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Male', max_length=50)),
                ('country', models.CharField(choices=[('DEFAULT', 'Select Country'), ('FRC', 'France'), ('JPA', 'Japan'), ('NGA', 'Nigeria'), ('USA', 'USA')], default='Select Country', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default='', max_length=50)),
                ('code', models.TextField()),
                ('language', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.author')),
            ],
        ),
    ]
