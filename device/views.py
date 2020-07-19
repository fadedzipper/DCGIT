from django.shortcuts import render
from rest_framework import generics
from device import models,serializers
from django.shortcuts import get_object_or_404
# Create your views here.

class DeviceView(generics.CreateAPIView):
    """
    新增设备

    #### 参数说明
    | 字段名称 | 描述 | 必须 | 类型 |
    | -- | -- | -- | -- |
    | serial | 设备序列号 | True | str |
    | mac | 设备mac地址 | True | str |
    | dev_passwd | 设备密码 | True | str|
    | name | 设备名称 | True | str |
    | info | 设备描述信息 | True | str |
    | x_index| 设备地图坐标 | True | str |
    | y_index | 设备地图坐标 | True | str |

    #### 响应字段说明
    | 字段名称 | 描述 | 类型 |
    | -- | -- | -- |
    | serial | 设备序列号 |str |
    | mac | 设备mac地址 | str |
    | name | 设备名称 | str |
    | info | 设备描述信息 | str |
    | x_index| 设备地图坐标 |  str |
    | y_index | 设备地图坐标 | str|
    | is_enable |是否可用| bool|
    | is_online |是否在线|bool|
    | is_register |是否激活|bool|
    | msg| 提示信息 | string |
    | code | 状态码 | int |

    ####注意：
    1 设备序号唯一标识一个设备.找不到改设备,返回400 ,提示：设备不存在
    2 设备is_register 为True时,已被激活,无法再次激活,返回400, 报错提示：设备已激活
    3 设备密码错误是,返回400,报错提示：设备秘钥错误

    #### 响应消息：
    | Http响应码 | 原因 | 响应模型 |
    | -- | -- | -- |
    | 201 | 添加成功 | 返回数据 |
    | 400 | 参数错误 | 参数错误 |
    | 500 | 请求失败 | 服务器内部错误 |
    """
    queryset = models.Device.objects.all()
    serializer_class = serializers.CreateDeviceSerialzer


class DeviceConfView(generics.UpdateAPIView):
    """
    修改设备配置

    #### 参数说明
    | 字段名称 | 描述 | 必须 | 类型 |
    | -- | -- | -- | -- |
    |id | 设备ID（在url中指定）|True  | int  |
    |PM25| 报警阈值  | True |  int |
    |PM10| 报警阈值  | True  | int  |
    |SO2| 报警阈值  | True  | int  |
    |NO2| 报警阈值  | True  | int  |
    |CO | 报警阈值  | True  |  int |
    |O3| 报警阈值  | True   | int  |
    |WindSpeed|报警阈值   | True  |  int |
    |Light|报警阈值   | True  | int  |
    |CO2| 报警阈值  | True  | int  |
    |Temperature| 报警阈值  | True  | int  |
    |Humidity | 报警阈值  | True  |  int |
    |AirPressure| 报警阈值  | True  | float  |
    |Frequency| 上报频率   | True  | int（秒数）|


    #### 响应字段说明

    | 字段名称 | 描述 | 类型 |
    | -- | -- | -- |
    |PM25| 报警阈值  |  int |
    |PM10| 报警阈值  |  int |
    |SO2 | 报警阈值  |  int |
    |NO2 | 报警阈值  |  int |
    |CO  | 报警阈值  |  int |
    |O3  | 报警阈值  |  int |
    |WindSpeed|报警阈值   |   int |
    |Light    |报警阈值   |   int |
    |CO2      | 报警阈值  |  int  |
    |Temperature| 报警阈值  | int |
    |Humidity   | 报警阈值  | int |
    |AirPressure| 报警阈值  | float  |
    |Frequency  | 上报频率  |  int（秒数）|
    |update_status| 设备同步状态| True 设备已同步 False 设备未同步|
    |update_time  |更新时间     |datetime|
    |device_update_time|设备同步时间|datetime|
    | msg  | 提示信息 | string |
    | code | 状态码   | int    |



    #### 响应消息：
    | Http响应码 | 原因 | 响应模型 |
    | -- | -- | -- |
    | 201 | 修改成功 | 返回数据 |
    | 400 | 参数格式错误 | 参数格式错误 |
    | 503 | 无法连接采集服务器 | 发送命令失败 |
    """

    queryset = models.DeviceConf.objects.all()
    serializer_class = serializers.DeviceConfSerialzer

    def get_object(self):
        id = self.kwargs['pk']     # id  ==> pkv  { 'pk':1}
        object = get_object_or_404(models.DeviceConf,device_id=id)
        return object


 #  devices/1/conf  put



