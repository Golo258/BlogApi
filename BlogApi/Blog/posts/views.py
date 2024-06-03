from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework.serializers import Serializer
from django.shortcuts import get_object_or_404, render
from drf_yasg.utils import swagger_auto_schema

from .models import Post
from .serializers import PostSerializer
from accounts.serializers import CurrentUserPostsSerializer
from .permissions import ReadOnly, AuthorOrReadOnly


class CustomPaginator(PageNumberPagination):
    page_size = 3
    page_query_param = "page"
    page_size_query_param = "page_size"


class HomePageApiVIew(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class  = Serializer
    @swagger_auto_schema(
        operation_summary="Home Page Create View",
        operation_description="This returns simple massge with your own data concatenated",
    )
    def post(self, request):
        request_data = request.data
        response = {"message": "Its a homepage", "data": request_data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    @swagger_auto_schema(
        operation_summary="Home Page Retrieve View",
        operation_description="This returns simple massge",
    )
    def get(self, request):
        response = {"message": "It's a homepage "}
        return Response(data=response, status=status.HTTP_200_OK)


class PostRetrieveViewSet(viewsets.ViewSet):
    """
    View of listing available posts
    """

    permission_classes = [ReadOnly]

    @swagger_auto_schema(
        operation_summary="List Posts Viewset",
        operation_description="This returns list of all posts but with usage of viewsets",
    )
    def list(self, request: Request):
        queryset = Post.objects.all()
        serializer = PostSerializer(instance=queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Get Post Viewset",
        operation_description="This retrieves post based on its id",
    )
    def retrieve(self, request: Request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=post)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostListCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)

    @swagger_auto_schema(
        operation_summary="List Posts",
        operation_description="This returns list of all posts for authenticated user",
    )
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create Post",
        operation_description="This creates new post for authenticated user",
    )
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin):
    """
    View of updating post by given id and request body
    """

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    @swagger_auto_schema(
        operation_summary="Update Post",
        operation_description="This updates post by its id",
    )
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PostRemoveView(generics.GenericAPIView, mixins.DestroyModelMixin):
    """
    View of removing post by given id
    """

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    @swagger_auto_schema(
        operation_summary="Remove Post",
        operation_description="This removes post by its id",
    )
    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
@swagger_auto_schema(
    operation_summary="Get Author Posts",
    operation_description="This retrieve posts based on its author",
)
def get_posts_for_current_user(request: Request):
    user = request.user
    serializer = CurrentUserPostsSerializer(instance=user, context={"request": request})
    return Response(data=serializer.data, status=status.HTTP_200_OK)


class AuthorPostLists(generics.GenericAPIView, mixins.ListModelMixin):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorOrReadOnly]

    def get_queryset(self):
        username = (
            self.request.query_params.get("username") or None
        )  # /?username = author_username

        queryset = Post.objects.all()
        if username is not None:
            return Post.objects.filter(author__username=username)
        else:
            return queryset

    @swagger_auto_schema(
        operation_summary="Get List of Author Posts",
        operation_description="This retrieve posts based on its author",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
