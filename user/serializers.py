from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserSerizalizer(serializers.ModelSerializer):

    date_joined = serializers.DateTimeField(format("%Y-%m-%d %H:%M:%S"),input_formats=["%Y-%m-%d %H:%M:%S",],required=False)
    last_login = serializers.DateTimeField(format("%Y-%m-%d %H:%M:%S"),input_formats=["%Y-%m-%d %H:%M:%S",],required=False)
    gender = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id','username','password','last_name','gender','num','tel','email','info',\
                  'is_active','date_joined','last_login']
        # exclude = ['first_name','is_staff']
        extra_kwargs = {
            'password':{'write_only':True},
            'date_joined':{'read_only':True,'required':False},
            'last_login': {'read_only': True,'required':False},
            'info':{"required":False}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def get_gender(self,obj):
        return obj.get_gender_display()



# class UserUpdateSerizalizer(serializers.ModelSerializer):
class UserUpdateSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','last_name','gender','num','tel','email','info','is_active']





class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):

        data = super().validate(attrs)

        user = self.user
        data['id'] = user.id
        data['username'] = user.username
        data['last_name'] = user.last_name
        data['is_superuser'] = user.is_superuser
        data['perms'] = user.get_all_permissions()
        data['group'] = user.groups.all().values('id','name')

        return data




