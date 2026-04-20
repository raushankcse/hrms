from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import Token

from accounts.jwt_utils import blacklist_key
from accounts.redis_client import redis_client


class CustomJWTAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        if redis_client.get(blacklist_key(raw_token)):
            raise AuthenticationFailed("Token is blacklisted")
        return super().get_validated_token(raw_token)