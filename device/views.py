from django.shortcuts import render
from django.db.models import Avg
from device.utils import getAQI
from rest_framework import generics,views,status
from device import models,serializers
import datetime
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import FilterSet
from rest_framework.response import Response


class MyPagination(PageNumberPagination):

    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class DevicePostView(generics.CreateAPIView):
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


class DevicePostConfView(generics.CreateAPIView):
    pass


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


class DeviceUnableView(generics.DestroyAPIView):

    queryset = models.Device.objects.all()
    serializer_class = serializers.Device_unableSerializer

    def get_object(self):
        id = self.kwargs['pk']     # id  ==> pkv  { 'pk':1}
        object = get_object_or_404(models.Device,id=id)
        return object

    def destroy(self, request, *args, **kwargs):

        device = self.get_object()
        device.is_enable = 0
        device.save()

        return  Response({'msg':"冻结成功","code":200},status=status.HTTP_200_OK)


class DevicelistView(generics.ListAPIView):

    pagination_class = MyPagination
    queryset = models.Device.objects.all().order_by('id')
    serializer_class = serializers.DeviceSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    # filterset_fields = ('gender', 'is_active')
    search_fields = ('serial', 'name')


class DeviceupdateView(generics.UpdateAPIView):

    queryset = models.Device.objects.all().order_by('id')
    serializer_class = serializers.DeviceUpdateSerializer

    def get_object(self):
        id = self.kwargs['pk']
        object = get_object_or_404(models.Device, id = id)
        return object


class DeviceConflistView(generics.ListAPIView):

    pagination_class = MyPagination
    queryset = models.DeviceConf.objects.all().order_by('id')
    serializer_class = serializers.DeviceconflistSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    # filterset_fields = ('gender', 'is_active')
    # search_fields = ('serial', 'name')


class DeviceAlarmdatalistView(generics.ListAPIView):

    pagination_class = MyPagination
    queryset = models.AlarmData.objects.all().order_by('id')
    serializer_class = serializers.DevicealarmlistSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    # filterset_fields = ('gender', 'is_active')
    search_fields = ('device',)


class DeviceAlarmdataupdateView(generics.DestroyAPIView):

    queryset = models.Device.objects.all().order_by('id')
    serializer_class = serializers.DevicealarmupdateSerializer

    def get_object(self):
        id = self.kwargs['pk']
        object = get_object_or_404(models.AlarmData, id = id)
        return object

    def destroy(self, request, *args, **kwargs):

        alarm = self.get_object()
        alarm.status = 1
        alarm.dealwith_time = datetime.datetime.now()
        alarm.save()

        return  Response({'msg':"处理成功","code":200},status=status.HTTP_200_OK)


class DeviceRealdatalistView(generics.ListAPIView):

    pagination_class = MyPagination
    queryset = models.DeviceData.objects.all().order_by('id')
    serializer_class = serializers.DevicerealdatalistSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    # filterset_fields = ('gender', 'is_active')
    # search_fields = ('serial', 'name')


class DeviceHistorydatalistView(generics.ListAPIView):

    pagination_class = MyPagination
    queryset = models.DeviceHistoryData.objects.all().order_by('-id')
    serializer_class = serializers.DevicehistorydatalistSerializer
    # filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filterset_fields = ('device', )
    # search_fields = ('serial', 'name')

    # def list(self, request, *args, **kwargs):
    #
    #     dev_id = models.DeviceHistoryData.device.get(serial=)



class GetAQIView(views.APIView):

    def get(self,request,*args,**kwargs):
        # 获取一小时的数据
        end_time = datetime.datetime.now()
        start_time = datetime.datetime.now()-datetime.timedelta(hours=1)
        # time__gte=start_time  因为我的数据库里近一小时没数据,,开始时间的条件我这里我先去掉了,,大家有数据的话加上
        data = models.DeviceHistoryData.objects.filter(time__lte=end_time) \
            .values('device_id').annotate(PM25=Avg('PM25'),PM10=Avg('PM10'),SO2=Avg('SO2'),NO2=Avg('NO2'),CO=Avg('CO'),O3=Avg('O3')) \
            .values('device_id','PM25','PM10','SO2','NO2','CO','O3')

        # print(data)
        # [{"device_id":"","PM25":234...},{} ]


        # 计算API
        for d in data:
            print(d)
            d["IAQIPM25"] = getAQI(d["PM25"],"PM25")
            d["IAQIPM10"] = getAQI(d["PM10"], "PM10")
            d["IAQISO2"] = getAQI(d["SO2"], "SO2")
            d["IAQINO2"] = getAQI(d["NO2"], "NO2")
            d["IAQICO"] = getAQI(d["CO"], "CO")
            d["IAQIO3"] = getAQI(d["O3"], "O3")

            # 计算最大AQI
            AQIlist =[d["IAQIPM25"],d["IAQIPM10"],d["IAQISO2"],d["IAQINO2"],d["IAQICO"],d["IAQIO3"]]
            index = AQIlist.index(max(AQIlist))
            d["AQI"] = AQIlist[index]

            # 添加描述
            type_list = ['PM25','PM10','SO2','NO2','CO','O3']
            d['desc'] = "{} 为主要污染物。".format(type_list[index])


        # 计算排名 默认从小到大,  reverse=True 从大到小
        data = sorted(data, key=lambda d: d['AQI'])
        for i in range(0,len(data)):
            data[i]["rank"] = i+1

        return Response(data={'msg': "请求成功", "code": 200, "data": data}, status=status.HTTP_200_OK)


# class AlarmViewSet(ModelViewSet):
#     serializer_class = AlarmDataSerialzer
#     queryset = AlarmData.objects.all().order_by('id')
