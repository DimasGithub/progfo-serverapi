from rest_framework import serializers
from forum.models import Forum, Groupforum, Tags


class SerializerForum(serializers.ModelSerializer):
    class Meta:
        model = Forum
        field = '__all__'


class SerializerGroupForum(serializers.ModelSerializer):
    class Meta:
        model = Groupforum
        field = '__all__'


class SerializerTags(serializers.ModelSerializer):
    class Meta:
        model = Tags,
        field = '__all__'
