from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
# Create your views here.
from . import serializers,models
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import  PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

# 01 用户列表 完成
# 02 用户详情
# 03 编辑用户
# 04 冻结用户
# 05 重置密码

class SelfPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class UserModelViewSet(ModelViewSet):

    serializer_class = serializers.UserSerizalizer
    queryset = models.User.objects.all().order_by('id')
    pagination_class = SelfPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter ]
    filterset_fields = ('gender', 'is_active')
    search_fields = ('username','email','num','info')

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'update' or self.action == 'partial_update' :
            return serializers.UserUpdateSerizalizer
        else:
            return serializers.UserSerizalizer

    def list(self, request, *args, **kwargs):
        """
            用户列表

            #### 参数说明
            | 字段名称 | 描述 | 必须 | 类型 |
            | -- | -- | -- | -- |
            | page | 分页页码 | False | int |
            | page_size | 分页大小 | False | int |
            | gender |过滤条件：性别 (1男,2女) |False|int|
            | is_active |过滤条件：是否激活 (true激活,false冻结) |False|int|
            | search|模糊匹配，匹配字段('username','email','num','info')| False|str|



            #### 响应字段说明
            | 字段名称 | 描述 | 类型 |
            | -- | -- | -- |
            | id| 用户ID | -- | int |
            | username | 用户名 | -- | str |
            | last_name | 昵称 | string |
            | last_login| 最后登录时间 | Y-%m-%d %H:%M:%S |
            | date_joined | 创建时间 | Y-%m-%d %H:%M:%S |
            | is_superuser | 是否是超级用户 | int |
            | is_active| 是否冻结 | int |
            | email | 邮箱 | str|
            | tel| 电话 | str |
            | num | 工号 |  str |
            | gender | 性别 |  str |
            | info| 备注 |  int |

            #### 注意说明：
            无

            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | 200 | 请求成功 | 返回数据 |
            | 400 | 参数格式错误 | 参数格式错误 |
            | 500 | 请求失败 | 服务器内部错误 |
            """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        新增用户

        #### 参数说明
        | 字段名称 | 描述 | 必须 | 类型 |
        | -- | -- | -- | -- |
        | username | 用户名 | True | str |
        | password | 密码 | True | str |
        | last_name | 昵称 | True | str|
        | email | 邮箱 | True | str |
        | tel | 电话 | True | str |
        | num | 工号 | True | str |
        | gender | 性别(1男 2女) | True | int |
        | info | 备注信息 | False | int |
        | is_active | 账户状态(1 冻结 2 激活）| False |int|



        #### 响应消息：
        | Http响应码 | 原因 | 响应模型 |
        | -- | -- | -- |
        | 201 | 添加成功 | 返回数据 |
        | 400 | 参数格式错误 | 参数格式错误 |
        | 500 | 请求失败 | 服务器内部错误 |
        """
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
           冻结用户

           #### 参数说明
           | 字段名称 | 描述 | 必须 | 类型 |
           | -- | -- | -- | -- |
           | id| 用户id | True | int |

           #### 响应字段说明
           | 字段名称 | 描述 | 类型 |
           | -- | -- | -- |
           | msg| 提示信息 | string |
           | code | 状态码 | int |


           #### 注意说明：
           无

           #### 响应消息：
           | Http响应码 | 原因 | 响应模型 |
           | -- | -- | -- |
           | 200 | 冻结成功 | -- |
           | 400 | 参数格式错误 | 参数格式错误 |
           | 500 | 请求失败 | 服务器内部错误 |
           """
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(data={'msg':"成功冻结","code":200},status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        """
            修改用户信息

            #### 参数说明
            | 字段名称 | 描述 | 必须 | 类型 |
            | -- | -- | -- | -- |
            | id | 模型id | True | int |
            | last_name | 昵称 | True | str|
            | email | 邮箱 | True | str |
            | tel | 电话 | True | str |
            | num | 工号 | True | str |
            | gender | 性别(1男 2女) | True | int |
            | info | 备注信息 | True | int |
            | is_active | 账户状态(0 冻结 1 激活）| True |int|


            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | 200 | 修改成功 |修改成功|
            | 404 | 未找到 | 未找到|
            | 500 | 请求失败 | 服务器内部错误 |
            """
        return super().update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
            用户详情

            #### 参数说明
            | 字段名称 | 描述 | 必须 | 类型 |
            | -- | -- | -- | -- |
            | id | 模型id | True | int |


            #### 响应字段说明
            | 字段名称 | 描述 | 类型 |
            | -- | -- | -- |
            | id| 用户ID | -- | int |
            | username | 用户名 | -- | str |
            | last_name | 昵称 | string |
            | last_login| 最后登录时间 | Y-%m-%d %H:%M:%S |
            | date_joined | 创建时间 | Y-%m-%d %H:%M:%S |
            | is_superuser | 是否是超级用户 | int |
            | is_active| 是否冻结 | int |
            | email | 邮箱 | str|
            | tel| 电话 | str |
            | num | 工号 |  str |
            | gender | 性别 |  str |
            | info| 备注 |  int |

            #### 注意说明：
            无

            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | 200 | 请求成功 | 返回数据 |
            | 400 | 参数格式错误 | 参数格式错误 |
            | 500 | 请求失败 | 服务器内部错误 |
            """
        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
            修改用户信息(部分更新)

            #### 参数说明
            | 字段名称 | 描述 | 必须 | 类型 |
            | -- | -- | -- | -- |
            | id | 模型id | True | int |
            | last_name | 昵称 | False | str|
            | email | 邮箱 | False | str |
            | tel | 电话 | False | str |
            | num | 工号 | False | str |
            | gender | 性别(1男 2女) | False | int |
            | info | 备注信息 | False | int |
            | is_active | 账户状态(0 冻结 1 激活）| False |int|


            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | 200 | 修改成功 |修改成功|
            | 404 | 未找到 | 未找到|
            | 500 | 请求失败 | 服务器内部错误 |
            """
        return super().partial_update(request, *args, **kwargs)


class LoginView(TokenObtainPairView):

    serializer_class = serializers.LoginSerializer
