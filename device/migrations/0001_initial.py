# Generated by Django 2.2.6 on 2020-07-22 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='设备报警类型')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', models.CharField(default='', max_length=100, verbose_name='设备mac地址')),
                ('serial', models.CharField(default='', max_length=100, unique=True, verbose_name='设备序列号')),
                ('is_register', models.BooleanField(default=False, verbose_name='是否激活（是否由前端激活）')),
                ('is_enable', models.BooleanField(default=False, verbose_name='可用状态（故障）')),
                ('is_online', models.BooleanField(default=False, verbose_name='在线状态（心跳包监控在线状态）')),
                ('register_time', models.DateTimeField(auto_now_add=True, verbose_name='设备注册时间')),
                ('active_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='设备激活时间')),
                ('last_login_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='设备最上线时间')),
                ('last_logout_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='设备最后下线时间')),
                ('name', models.CharField(default='', max_length=100, null=True, verbose_name='设备名称')),
                ('info', models.CharField(default='', max_length=100, null=True, verbose_name='设备描述')),
                ('x_index', models.CharField(default='', max_length=50, null=True, verbose_name='位置')),
                ('y_index', models.CharField(default='', max_length=50, null=True, verbose_name='位置')),
                ('is_bind', models.BooleanField(default=False, null=True, verbose_name='设备是否绑定到网格')),
                ('grid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='grid.Grid')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceSecret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_passwd', models.CharField(default='', max_length=100, verbose_name='设备秘钥')),
                ('dev_key', models.CharField(default='', max_length=100, verbose_name='设备通信秘钥')),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='device.Device')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceHistoryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PM25', models.IntegerField(default=0)),
                ('PM10', models.IntegerField(default=0)),
                ('SO2', models.IntegerField(default=0)),
                ('NO2', models.IntegerField(default=0)),
                ('CO', models.IntegerField(default=0)),
                ('O3', models.IntegerField(default=0)),
                ('WindSpeed', models.IntegerField(default=0)),
                ('WindDirection', models.CharField(default='', max_length=100)),
                ('Light', models.IntegerField(default=0)),
                ('CO2', models.IntegerField(default=0)),
                ('Temperature', models.IntegerField(default=0)),
                ('Humidity', models.IntegerField(default=0)),
                ('AirPressure', models.FloatField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='device.Device')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PM25', models.IntegerField(default=0)),
                ('PM10', models.IntegerField(default=0)),
                ('SO2', models.IntegerField(default=0)),
                ('NO2', models.IntegerField(default=0)),
                ('CO', models.IntegerField(default=0)),
                ('O3', models.IntegerField(default=0)),
                ('WindSpeed', models.IntegerField(default=0)),
                ('WindDirection', models.CharField(default='', max_length=100)),
                ('Light', models.IntegerField(default=0)),
                ('CO2', models.IntegerField(default=0)),
                ('Temperature', models.IntegerField(default=0)),
                ('Humidity', models.IntegerField(default=0)),
                ('AirPressure', models.FloatField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='device.Device')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PM25', models.IntegerField(default=0, verbose_name='pm2.5阈值')),
                ('PM10', models.IntegerField(default=0, verbose_name='pm10阈值')),
                ('SO2', models.IntegerField(default=0)),
                ('NO2', models.IntegerField(default=0)),
                ('CO', models.IntegerField(default=0)),
                ('O3', models.IntegerField(default=0)),
                ('WindSpeed', models.IntegerField(default=0)),
                ('Light', models.IntegerField(default=0)),
                ('CO2', models.IntegerField(default=0)),
                ('Temperature', models.IntegerField(default=0)),
                ('Humidity', models.IntegerField(default=0)),
                ('AirPressure', models.FloatField(default=0)),
                ('Frequency', models.IntegerField(default=0, verbose_name='采集平率')),
                ('update_status', models.BooleanField(default=0, verbose_name='设备同步状态')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('device_update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='设备同步时间')),
                ('device_id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='device.Device')),
            ],
        ),
        migrations.CreateModel(
            name='AlarmData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='', max_length=100, verbose_name='报警值')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='报警时间')),
                ('status', models.BooleanField(default=False, verbose_name='处理状态（已处理/未处理）')),
                ('dealwith_time', models.DateTimeField(default=None, null=True, verbose_name='处理时间')),
                ('alarmtype', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='device.AlarmType', verbose_name='报警类型')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='device.Device')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='处理人')),
            ],
        ),
    ]
