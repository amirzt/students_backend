from rest_framework import serializers

from Users.models import CustomUser, Student


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['password', 'phone']
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, **kwargs):
        user = CustomUser(phone=self.validated_data['phone'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class GetUsersInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['name', 'id']


class GetStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['user', 'id']
