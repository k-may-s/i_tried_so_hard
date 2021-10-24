from rest_framework import views, status
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from .models import User
from .serializers import UserSerializer


class AuthView(views.APIView):

    def create_user(self, request):
        login_data = UserSerializer(data=request.data)
        if login_data.is_valid():
            login_data.create(data=request.data)
            return Response({'status': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

    def authenticate_user(self, request):
        try:
            login = request.data['login']
            password = request.data['password']
            user = User.objects.get(login=login)
            if user:
                if user.password == password:
                    try:
                        payload = jwt_payload_handler(user)
                        token = jwt_encode_handler(payload)
                        return Response({'status': status.HTTP_200_OK, 'token': token}, status=status.HTTP_200_OK)
                    except Exception as e:
                        raise e
                else:
                    return Response({'status': status.HTTP_200_OK,
                                    'error_message': 'Введен неправильный пароль'},
                                    status=status.HTTP_200_OK)
            else:
                return Response({'status': status.HTTP_200_OK,
                                 'error_message': 'Пользователь с указанными данными не найден в системе'},
                                status=status.HTTP_200_OK)
        except KeyError:
            return Response({'status': status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)


