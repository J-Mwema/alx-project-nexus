from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)


    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role')
        extra_kwargs = {
                'role': {'required': False}
        }

    def create(self, validated_data):
        role = validated_data.pop('role', User.Role.JOBSEEKER)

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=role
        )
        return user

    def validate_role(self, value):
        if value == User.Role.ADMIN:
            raise serializers.ValidationError(
                    "Admin accounts cannot be created via registration."
            )
        return value


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Custom claims
        token['username'] = user.username
        token['role'] = user.role

        return token
