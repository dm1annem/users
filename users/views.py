from rest_framework.views import APIView
from rest_framework.response import Response
from .serialisers import UserSerialiser

class RegisterView(APIView):
    def post(self, request):
        serialiser = UserSerialiser(data=request.data)
        serialiser.is_valid(raise_exception=True)
        serialiser.save()
        return Response(serialiser.data)

