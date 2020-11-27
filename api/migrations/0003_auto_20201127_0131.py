# Generated by Django 3.1.3 on 2020-11-27 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201127_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='congressman',
            name='commission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.commission'),
        ),
        migrations.AlterField(
            model_name='congressman',
            name='politicalParty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.politicalparty'),
        ),
    ]
