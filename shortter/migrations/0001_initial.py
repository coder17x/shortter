# Generated by Django 3.0.5 on 2020-04-23 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('lnk_id', models.SmallIntegerField(db_column='lnk_id', primary_key=True, serialize=False)),
                ('lnk_short_name', models.CharField(max_length=16)),
                ('lnk_full_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Links',
            },
        ),
    ]
