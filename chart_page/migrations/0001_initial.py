# Generated by Django 3.0.6 on 2020-06-11 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gu', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Traffic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_car', models.PositiveIntegerField()),
                ('parking_lot', models.PositiveIntegerField()),
                ('bike', models.PositiveIntegerField()),
                ('bus', models.PositiveIntegerField()),
                ('trail', models.PositiveIntegerField()),
                ('bus_trail', models.PositiveIntegerField()),
                ('mycar', models.PositiveIntegerField()),
                ('gu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chart_page.Goo')),
            ],
        ),
        migrations.CreateModel(
            name='SeoulData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('safety', models.FloatField()),
                ('medical', models.FloatField()),
                ('medical_room', models.FloatField()),
                ('environment', models.FloatField()),
                ('traffic', models.FloatField()),
                ('education', models.FloatField()),
                ('gu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chart_page.Goo')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('garden', models.FloatField()),
                ('element', models.FloatField()),
                ('middle', models.FloatField()),
                ('high', models.FloatField()),
                ('garden_num', models.FloatField()),
                ('element_num', models.FloatField()),
                ('middle_num', models.FloatField()),
                ('high_num', models.FloatField()),
                ('garden_gyo', models.FloatField()),
                ('element_gyo', models.FloatField()),
                ('middle_gyo', models.FloatField()),
                ('high_gyo', models.FloatField()),
                ('gu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chart_page.Goo')),
            ],
        ),
    ]
