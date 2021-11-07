from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import UserPassword, UserProfile


class UserPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPassword
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, validated_data):
        try:
            UserProfile.objects.get(username=validated_data)
            raise ValidationError('User is exist')
        except UserProfile.DoesNotExist:
            return validated_data

    def create(self, validated_data):
        user = UserProfile.objects.create(
            username=validated_data['username'],

        )

        u = UserPassword.objects.create(password=validated_data['password'], user=user)
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, write_only=True)
    password_new = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = UserPassword
        fields = ('username', 'password', 'password_new')
        extra_kwargs = {'username': {'write_only': True},
                        'password': {'write_only': True}
                        }

    def validate_username(self, validated_data):
        try:
            UserProfile.objects.get(username=validated_data)
            return validated_data
        except UserPassword.DoesNotExist:
            raise ValidationError('User is not exist')

    def create(self, validated_data):
        user = UserProfile.objects.get(username=validated_data['username'])
        pass_user = UserPassword.objects.filter(user=user)
        for u in pass_user:
            if validated_data['password'] in u.password:
                password_u = UserPassword.objects.create(
                    password=validated_data['password_new'],
                    user=user
                )
                return password_u

        raise ValidationError('password wrong!!!')
