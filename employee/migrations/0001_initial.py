# Generated by Django 3.1.4 on 2020-12-04 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
            ],
            options={
                'ordering': ('username',),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=20, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/%Y/%m/%d/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-salary',),
            },
        ),
    ]
