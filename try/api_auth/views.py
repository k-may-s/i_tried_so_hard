import random
import string

from rest_framework import views
from rest_framework.response import Response

from .models import AuthUser
from .serializers import AuthUserSerializer


class AuthView(views.APIView):

    def post(self, request):
        login_data = AuthUserSerializer(data=request.data)
        if login_data.is_valid():
            login_data.save(login=request.data.get("login"), password=request.data.get("password"))
            response = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 100)))
            return Response({"response": response})
        else:
            return Response({'response': "Something wrong... Again..."})
