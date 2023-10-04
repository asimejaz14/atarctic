from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST

from common.enums import USER_SORTING_KEYS, Status
from common.utils import get_default_query_param
from .models import User
from .serializers import UserSerializer


class UserController:
    @classmethod
    def get_user(cls, request, user_id=None):
        try:
            if user_id:
                user = User.objects.filter(id=user_id).first()
                if not user:
                    return Response(status=status.HTTP_204_NO_CONTENT)
                serializer = UserSerializer(user)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            kwargs = {}
            order_by = get_default_query_param(request, "order_by", "created_at")
            order = get_default_query_param(request, "order", "desc")

            if order == "asc":
                sort = USER_SORTING_KEYS[order_by]
            else:
                sort = "-" + USER_SORTING_KEYS[order_by]

            kwargs['status'] = Status.ACTIVE
            users = User.objects.filter(**kwargs).order_by(sort)
            serializer = UserSerializer(users, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data=str(e), status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def create_user(cls, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(data=str(e), status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def update_user(cls, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(data=str(e), status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def delete_user(cls, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(data=None, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(data=str(e), status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def login(cls, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = User.objects.get(username=username, password=password)
            if user:
                return Response(data=user.username, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(data=str(e), status=HTTP_500_INTERNAL_SERVER_ERROR)
