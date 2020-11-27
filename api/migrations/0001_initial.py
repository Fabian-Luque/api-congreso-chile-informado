# Generated by Django 3.1.3 on 2020-11-27 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Congressman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('district', models.IntegerField()),
                ('num_congress', models.IntegerField()),
                ('entity', models.CharField(max_length=50)),
                ('suplent', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('foto', models.URLField(max_length=500)),
                ('commission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.commission')),
            ],
        ),
        migrations.CreateModel(
            name='PoliticalParty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('descripton', models.TextField()),
                ('status', models.CharField(max_length=50)),
                ('orientation', models.SmallIntegerField()),
                ('establish', models.DateField()),
                ('president', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='politicalparty_president', to='api.congressman')),
            ],
        ),
        migrations.AddField(
            model_name='congressman',
            name='politicalParty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.politicalparty'),
        ),
        migrations.AddField(
            model_name='commission',
            name='president',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='commission_president', to='api.congressman'),
        ),
    ]
