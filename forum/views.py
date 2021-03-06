from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from forum.serializer import SerializerForum, SerializerGroupForum, SerializerTags
from rest_framework.response import Response
from forum.models import Forum, Groupforum, Tags


@api_view(['GET'])
def ShowDataAll(request):
    query = Forum.object.all()
    serializer = SerializerForum(query, many=True)
    return Response(serializer.data)
