# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-16 04:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Boardgame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreatedTime', models.DateTimeField(auto_now_add=True)),
                ('ModifiedTime', models.DateTimeField(auto_now=True)),
                ('BGGRef', models.URLField(blank=True, null=True)),
                ('Name', models.CharField(max_length=100)),
                ('UPC', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'ordering': ['Name'],
            },
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CheckedOutTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('CheckedInTime', models.DateTimeField(blank=True, null=True)),
                ('ModifiedTime', models.DateTimeField(auto_now=True)),
                ('PreConditionNote', models.CharField(blank=True, max_length=500, null=True)),
                ('PostConditionNote', models.CharField(blank=True, max_length=500, null=True)),
                ('PostWeight', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
            ],
            options={
                'ordering': ['-CheckedInTime', 'CheckedOutTime'],
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreatedTime', models.DateTimeField(auto_now_add=True)),
                ('ModifiedTime', models.DateTimeField(auto_now=True)),
                ('RFIDTag', models.BigIntegerField(blank=True, null=True)),
                ('PreWeight', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('RegisteredPersonalGame', models.BooleanField(default=False)),
                ('AvailableAtEvent', models.BooleanField(default=False)),
                ('Shelved', models.BooleanField(default=False)),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
                ('Boardgame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collections.Boardgame')),
            ],
            options={
                'ordering': ['Boardgame', 'Person'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreatedTime', models.DateTimeField(auto_now_add=True)),
                ('ModifiedTime', models.DateTimeField(auto_now=True)),
                ('BadgeNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('FirstName', models.CharField(blank=True, max_length=50, null=True)),
                ('LastName', models.CharField(max_length=50)),
                ('IsBusiness', models.BooleanField(default=False)),
                ('Suffix', models.CharField(blank=True, max_length=10, null=True)),
                ('Phone', models.CharField(blank=True, max_length=15, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
                ('State', models.CharField(blank=True, max_length=2, null=True)),
                ('Zip', models.CharField(blank=True, max_length=5, null=True)),
                ('EmailAddress', models.EmailField(blank=True, max_length=254, null=True)),
                ('ReceiveNewsletter', models.BooleanField(default=False)),
                ('NewsletterFrequencyCode', models.CharField(blank=True, max_length=1, null=True)),
                ('AuthUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['LastName', 'FirstName'],
            },
        ),
        migrations.AddField(
            model_name='collection',
            name='Person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collections.Person'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='Attendee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collections.Person'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='BoardgameFromCollection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collections.Collection'),
        ),
        migrations.AddIndex(
            model_name='boardgame',
            index=models.Index(fields=['Name', 'BGGRef'], name='Collections_Name_2bedc3_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='boardgame',
            unique_together=set([('Name', 'BGGRef')]),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['LastName', 'FirstName'], name='Collections_LastNam_0e6bbf_idx'),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['BadgeNumber'], name='Collections_BadgeNu_8f1ad2_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('BadgeNumber',)]),
        ),
        migrations.AddIndex(
            model_name='collection',
            index=models.Index(fields=['Boardgame'], name='Collections_Boardga_915b7f_idx'),
        ),
        migrations.AddIndex(
            model_name='collection',
            index=models.Index(fields=['Person'], name='Collections_Person__9bfd33_idx'),
        ),
        migrations.AddIndex(
            model_name='collection',
            index=models.Index(fields=['Shelved'], name='Collections_Shelved_9c55d9_idx'),
        ),
        migrations.AddIndex(
            model_name='checkout',
            index=models.Index(fields=['CheckedOutTime', 'CheckedInTime'], name='Collections_Checked_559462_idx'),
        ),
        migrations.AddIndex(
            model_name='checkout',
            index=models.Index(fields=['BoardgameFromCollection'], name='Collections_Boardga_5fbfd3_idx'),
        ),
    ]
