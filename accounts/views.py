from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser

from accounts.jwt_utils import get_ttl, blacklist_key
from accounts.redis_client import redis_client
from accounts.serializers import LoginSerializer, RefreshTokenSerializer, UserListSerializer, AdminSetPasswordSerializer
from .permissions import IsAdminOnly

User = get_user_model()



# Create your views here.

class LoginApiView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]

            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            response = Response({
                "access" :str(access),

            }, status=status.HTTP_200_OK)

            response.set_cookie(
                key="refresh",
                value=str(refresh),
                httponly=True,
                samesite="Strict",
                secure=False,
                max_age=60*60*24,
            )

            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RefreshTokenView(APIView):
    def post(self, request):
        old_refresh_token = request.COOKIES.get("refresh")


        if not old_refresh_token:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:

            old_refresh = RefreshToken(old_refresh_token)

            user_id = old_refresh["user_id"]

            user = CustomUser.objects.get(id=user_id)



            # blacklist old token
            ttl = get_ttl(old_refresh)
            redis_client.set(
                blacklist_key(old_refresh_token),
                "1",
                ex=ttl,
            )


            new_refresh = RefreshToken.for_user(user)
            new_access = new_refresh.access_token




            response = Response({
                "access": str(new_access),
            })

            response.set_cookie(
                key="refresh",
                value=str(new_refresh),
                httponly=True,
                secure=False,
                samesite="Strict",
                max_age=get_ttl(new_refresh),
            )

            return response
        except Exception:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutApiView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh")

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)

                redis_client.set(
                    blacklist_key(refresh_token),
                    "1",
                    ex=get_ttl(token),
                )
            except:
                pass

        response = Response({"message" : "Successfully logged out"})
        response.delete_cookie("refresh")

        return response


class UserListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOnly ]

    def get(self, request):
        users = User.objects.all().only("id", "email", "role")
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

class AdminSetPasswordView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOnly]

    def post(self, request):
        serializer = AdminSetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.validated_data["user_id"]
        password = serializer.validated_data["password"]

        try:
            user = User.objects.get(id = user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        user.set_password(password)
        user.save()

        return Response(
            {"message": "Password updated successfully"},
            status=status.HTTP_200_OK
        )
    