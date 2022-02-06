# делал по видео https://www.youtube.com/watch?v=PUzgZrS_piQ&t=1446s

# import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.exceptions import AuthenticationFailed
from .serialisers import UserSerialiser
from .models import User
import datetime, jwt
from api.settings import SECRET_KEY

class RegisterView(APIView):
    def post(self, request):
        serialiser = UserSerialiser(data=request.data)
        serialiser.is_valid(raise_exception=True)
        serialiser.save()
        return Response(serialiser.data)

class LoginView(APIView):
    def post(self, request):
        # присваиваем в переменные данные пришедшие в запросе с клиента
        email = request.data['email']
        password = request.data['password']

        # ищем по емейлу пользователя
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('Пользователь не найден')

        if not user.check_password(password):
            raise AuthenticationFailed('Не верный пароль')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')   #   decode('utf-8') в видео было, а тут не получается

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'jwt': token}
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Пользователь не авторизован!')

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Пользователь с таким токеном не авторизован!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerialiser(user)
        return Response(serializer.data)
