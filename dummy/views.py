from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from users.views import (LoginAPIView)

class LoginView(APIView):

    def post(self, request):
        login = LoginAPIView()
        data = login.post(request)
        return Response(data, status=status.HTTP_200_OK)

