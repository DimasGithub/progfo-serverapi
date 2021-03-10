from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from forum.serializer import SerializerForum, SerializerGroupForum, SerializerTags
from rest_framework.response import Response
from forum.models import Forum, Groupforum, Tags


@api_view(['GET'])
def ShowDataAll(request):
    query = Forum.objects.all()
    serializer = SerializerForum(query, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ShowDetailData(request, id):
    query = Forum.objects.filter(id=id)
    serializer = SerializerForum(query, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def CreateData(request):
    serializer = SerializerForum(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def EditData(request, pk):
    data = Forum.objects.filter(id=pk)
    serializer = SerializerForum(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def DeleteData(request, pk):
    data = Forum.objects.get(id=pk).delete()
    return Response('success delete')
