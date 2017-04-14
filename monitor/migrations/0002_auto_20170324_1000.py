# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-24 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CpuJumps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context_switchs_per_second', models.IntegerField(verbose_name='\u6bcf\u79d2\u4e0a\u4e0b\u6587\u5207\u6362\u6b21\u6570')),
                ('interrupts_per_second', models.IntegerField(verbose_name='\u6bcf\u79d2\u4e2d\u65ad\u6b21\u6570')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CpuUtilization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_idle_time', models.CharField(max_length=16, verbose_name='CPU\u7a7a\u95f2\u767e\u5206\u6bd4')),
                ('cpu_user_time', models.CharField(max_length=16, verbose_name='CPU\u7528\u6237\u767e\u5206\u6bd4')),
                ('cpu_system_time', models.CharField(max_length=16, verbose_name='CPU\u7cfb\u7edf\u767e\u5206\u6bd4')),
                ('cpu_iowait_time', models.CharField(max_length=16)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiskUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_disk_space', models.CharField(max_length=16, verbose_name='\u78c1\u76d8\u603b\u7a7a\u95f4\u5927\u5c0f')),
                ('free_disk_space', models.CharField(max_length=16, verbose_name='\u78c1\u76d8\u5269\u4f59\u7a7a\u95f4\u5927\u5c0f')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=32, verbose_name='\u4e3b\u673a\u540d\u79f0')),
                ('ip', models.CharField(max_length=32, verbose_name='ip\u5730\u5740')),
                ('hostid', models.IntegerField(verbose_name='\u4e3b\u673aid')),
                ('available', models.IntegerField(default=0, verbose_name='\u662f\u5426\u53ef\u7528')),
            ],
        ),
        migrations.CreateModel(
            name='MemoryUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_memory', models.CharField(max_length=16, verbose_name='\u53ef\u7528\u5185\u5b58')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.Host')),
            ],
        ),
        migrations.CreateModel(
            name='Ping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ping', models.IntegerField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.Host')),
            ],
        ),
        migrations.AddField(
            model_name='diskusage',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.Host'),
        ),
        migrations.AddField(
            model_name='cpuutilization',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.Host'),
        ),
        migrations.AddField(
            model_name='cpujumps',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.Host', verbose_name='\u76d1\u63a7\u4e3b\u673a'),
        ),
    ]
