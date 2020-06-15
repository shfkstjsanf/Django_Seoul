# Generated by Django 3.0.6 on 2020-06-11 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chart_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvironmentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('park', models.FloatField()),
                ('garbage', models.FloatField()),
                ('dust', models.FloatField()),
                ('green', models.FloatField()),
                ('gu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chart_page.Goo')),
            ],
        ),
    ]
