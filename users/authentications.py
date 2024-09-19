from os import access
from typing import Optional, Tuple
from django.contrib.auth import get_user_model
from rest_framework.request import Request
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import Token

from rest_framework_simplejwt.authentication import AuthUser, JWTAuthentication
from .enums import TokenType
from .services import TokenService
from django.utils.translation import gettext_lazy as _
User = get_user_model()

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request: Request) -> Optional[Tuple[AuthUser, Token]]:
        header = self.get_header(request)
        if header is None:
            return None
        raw_token = self.get_raw_token(header)
        user, access_token = super().authenticate(request)
        if not self.is_valid_access_token(user, access_token):
            raise AuthenticationFailed(_('Access token yaroqsiz'))
        return user, access_token

    @classmethod
    def is_valid_access_token(cls, user: User, access_token: Token) -> bool:
            valid_access_token = TokenService.get_valid_tokens(user.id, TokenType.ACCESS)
            if (
                valid_access_token
                and  str(access_token).encode() not in valid_access_token
            ):
                raise AuthenticationFailed(_('Kirisih malumotlar yaroqsiz'))
            return True


