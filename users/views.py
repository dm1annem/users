from rest_framework.views import APIView
from rest_framework.response import Response
from .serialisers import UserSerialiser
from .models import User

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
        user = User.objects.filter('email').first()



