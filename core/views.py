from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from .models import Endereco
from .models import Estado
from .models import Cidade

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from core.api.serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated   


def buscar_cep(request):
    if request.method == 'POST':
        cep = request.POST.get('cep', "")

        endereco = Endereco.objects.buscar_cep(cep)

        return JsonResponse(endereco)


def on_change_pais(request):
    if request.method == 'POST':
        pais = request.POST.get('pais', 0)

        estados = Estado.objects.filter(pais=pais)

        estados_serializados = serializers.serialize('json', estados)
        return JsonResponse(estados_serializados, safe=False)


def on_change_estado(request):
    if request.method == 'POST':
        estado = request.POST.get('estado', 0)

        cidades = Cidade.objects.filter(estado=estado)

        cidades_serializadas = serializers.serialize('json', cidades)
        return JsonResponse(cidades_serializadas, safe=False)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('listar_oportunidade')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def resetar_senha(request):
    return render(request, 'resetar_senha.html', {})

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)