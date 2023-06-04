from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import *
from django.core.exceptions import PermissionDenied
from rest_framework.authentication import BasicAuthentication

####################################################################


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDestroyView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

################################################################


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class PostRetrieveView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        obj = super().get_object()
        if obj.is_private and obj.author != self.request.user:
            self.permission_denied(self.request)
        return obj



class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author:
            raise PermissionDenied("You do not have permission to update this post.")
        serializer.save()



class PostDestroyView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_destroy(self, serializer):
        if self.request.user != serializer.author:
            raise PermissionDenied("You do not have permission to delete this post.")
        serializer.delete()
        

###############################################################################################


class LikeListView(ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeCreateView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    


class LikeRetrieveView(RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer



class LikeUpdateView(UpdateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer



class LikeDestroyView(DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    

###############################################################################################
