from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView

from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


class PostListView(APIView):
    """
    View of listing available posts
    """

    serializer_class = PostSerializer

    def get(self, request: Request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = self.serializer_class(instance=posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostCreateView(APIView):
    """
    View of creation new post
    """

    serializer_class = PostSerializer

    def post(self, request: Request, *args, **kwargs):
        request_data = request.data
        serializer = self.serializer_class(data=request_data)

        if serializer.is_valid():
            serializer.save()
            response = {"message": "New Post Created", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostRetrieveView(APIView):
    """
    View of getting post by given id
    """

    serializer_class = PostSerializer

    def get(self, request: Request, post_id: int):
        post = get_object_or_404(Post, pk=post_id)
        serializer = self.serializer_class(instance=post)
        response = {"message": f"Post by id {post_id}", "data": serializer.data}
        return Response(data=response, status=status.HTTP_200_OK)


class PostUpdateView(APIView):
    """
    View of updating post by given id and request body
    """

    serializer_class = PostSerializer

    def put(self, request: Request, post_id: int):
        post = get_object_or_404(Post, pk=post_id)
        request_data = request.data
        serializer = self.serializer_class(instance=post, data=request_data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": f"Post with id: {post_id} updated",
                "data": serializer.data,
            }
            return Response(data=response, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostRemoveView(APIView):
    """
    View of removing post by given id
    """

    serializer_class = PostSerializer

    def delete(self, request: Request, post_id: int):
        post = get_object_or_404(Post, pk=post_id)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
