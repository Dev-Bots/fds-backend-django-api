from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers import LoginSerializer


class LoginTokenView(TokenObtainPairView):
    serializer_class = LoginSerializer
 