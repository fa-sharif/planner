from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import AnonymousUser, User
from channels.middleware import BaseMiddleware

@database_sync_to_async
def get_user(token):
    try:
        access_token = AccessToken(token)
        print("jjjjjjjjjjjjjjjjjjj")
        print(access_token)
        user = User.objects.get(id=access_token['user_id'])
        return user
    except Exception:
        return AnonymousUser()

class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query_string = scope['query_string'].decode()
        params = parse_qs(query_string)
        token = params.get('token', [None])[0]

        scope['user'] = await get_user(token)
        return await super().__call__(scope, receive, send)

def JWTAuthMiddlewareStack(inner):
    return JWTAuthMiddleware(inner)
