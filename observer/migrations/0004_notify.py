# Generated by Django 2.2.5 on 2019-09-15 19:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('observer', '0003_auto_20190915_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=30)),
                ('url', models.CharField(default='', max_length=100)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='observer.Site')),
            ],
        ),
    ]