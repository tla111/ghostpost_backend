# Generated by Django 3.1.4 on 2020-12-26 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('submission_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('name_post', models.BooleanField(choices=[(True, 'boast'), (False, 'roast')])),
            ],
        ),
    ]