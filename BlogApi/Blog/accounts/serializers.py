from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import CustomUser
from rest_framework.authtoken.models import Token


class SignUpSerializer(serializers.ModelSerializer):

    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "username", "password"]

    def validate(self, attributes):
        email_exists = CustomUser.objects.filter(email=attributes["email"]).exists()
        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs=attributes)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
