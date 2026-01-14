from .models import Client, News
from .serializers import ClientSerializer, NewsSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication


# Права
# class ReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS


# Пример своих прав только для клиентов
# class ReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         return requst.user.is_client



# ViewSets
# class ClientViewSet(viewsets.ModelViewSet):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
#     permission_classes = [IsAdminUser|ReadOnly]
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#
#
# class NewsViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAdminUser]
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
