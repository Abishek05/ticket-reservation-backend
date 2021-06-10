from rest_framework import serializers

from flight_reservation import models


class UserSerilaizer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        user = models.User(
            email=validated_data['email'],
            name=validated_data['name'],
            username=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user



