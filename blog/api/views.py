from django.http import HttpResponse,JsonResponse
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def view_post(request, format=None):
    if request.method == 'GET':
        query_post = Post.objects.all()
        serializer = PostSerializer(query_post, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def view_post_detail(request, pk, format=None):
    try:
        query_post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PostSerializer(query_post, many=False)
        return Response(serializer.data)
    elif request.method == 'Post':
        data = JSONParser().parse(request)
        serializer = PostSerializer(query_post , data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.error, status=400)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(instance=query_post, data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        query_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


