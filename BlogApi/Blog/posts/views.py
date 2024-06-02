from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView

from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class PostRetrieveViewSet(viewsets.ViewSet):
    """
    View of listing available posts
    """
    permission_classes = [IsAuthenticated]
    def list(self, request: Request):
        queryset = Post.objects.all()
        serializer = PostSerializer(instance=queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request: Request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=post)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostCreateView(generics.GenericAPIView, mixins.CreateModelMixin):
    """
    View of creation new post
    """

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin):
    """
    View of updating post by given id and request body
    """

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PostRemoveView(generics.GenericAPIView, mixins.DestroyModelMixin):
    """
    View of removing post by given id
    """

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
