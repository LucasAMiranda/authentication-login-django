from django.contrib.auth.backends import ModelBackend
from .models import Usuarios

class CPFBackend(ModelBackend):
    def authenticate(self, request, cpf=None, password=None, **kwargs):
        try:
            user = Usuarios.objects.get(cpf=cpf)
            if user.check_password(password):
                return user
        except Usuarios.DoesNotExist:
            return None
