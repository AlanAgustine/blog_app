from rest_framework import serializers
from blog.models import blogModel,userModel



class blogSerializers(serializers.ModelSerializer):
    class Meta:
        model=blogModel
        fields=(
            'title',
            'post',
            'user_id',
            'profile'

        )

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model=userModel
        fields=(
            'name',
            'email',
            'user_id',
            'password'

        )      