from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_authentication = JWTAuthentication()

    def __call__(self, request):
        try:
            user, token = self.jwt_authentication.authenticate(request)
            request.user = user
            request.token = token
        except AuthenticationFailed:
            pass

        response = self.get_response(request)

        return response
