from rest_framework import serializers
from api.models import User
from datetime import datetime


class GetCurrentDate(object):
    def __call__(self):
        return datetime.timestamp(datetime.now())


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'account', 'nickname', 'password', 'sex', 'email', 'phone', 'avatar', 'created_date', 'updated_date']

    account = serializers.RegexField(error_messages={
        'required': '请输入账户名信息！',
        'min_length': '账户名最少6位字符',
        'max_length': '账户名最多20位字符',
        'invalid': '账户名必须由大小写字母或数字构成!'
    }, regex=r"^[a-zA-Z0-9]{6,20}$", min_length=6, max_length=20)
    password = serializers.RegexField(error_messages={
        'required': '请输入密码！',
        'min_length': '密码最少8位字符',
        'max_length': '密码最多16位字符',
        'invalid': '密码必须同时包含大小写字母、数字、特殊符号(_.@!~?&)'
    }, regex=r"^[a-zA-Z0-9_.@!~?&]{8,16}$", min_length=8, max_length=16, style={'input_type': 'password'})
    email = serializers.EmailField(error_messages={
        'invalid': '请输入正确的邮箱信息！'
    })
    sex = serializers.ChoiceField(error_messages={
        'required': '请填写性别信息！'
    }, choices=User.Sex.choices)
    phone = serializers.RegexField(error_messages={
        'required': '请输入手机号！',
        'min_length': '仅支持中国大陆（+86）11位有效手机号码',
        'max_length': '仅支持中国大陆（+86）11位有效手机号码',
        'invalid': '请输入正确的手机号信息'
    }, regex=r"^1[356789][0-9]{9}$", min_length=11, max_length=11)
    created_date = serializers.HiddenField(default=GetCurrentDate())
    updated_date = serializers.HiddenField(default=GetCurrentDate())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data["sex"] == User.Sex.MAN:
            data["sex"] = "男"
        elif data["sex"] == User.Sex.WOMAN:
            data["sex"] = "女"
        else:
            data["sex"] = ""
        return data

