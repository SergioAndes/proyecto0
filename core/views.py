from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from core import serializers
from core.models import Evento, Categoria
from core.serializers import EventoSerializer, UsuarioSerializer, CategoriaSerializer


class EventsView(APIView):
    def get(self, request, *args, **kwargs):
        idUser = self.kwargs.get('idUser', None)
        eventsList = Evento.objects.filter(usuario=idUser)
        serializer = EventoSerializer(eventsList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        print("sdfsdfsdfsfdds")
        requestData = request.data
        usuario = requestData.pop('usuario', None)
        categoria = requestData.pop('categoria', None)
        print(requestData.pop('token', None))
        valid_data = VerifyJSONWebTokenSerializer().validate(requestData.pop('token', None))
        categoriaObj = Categoria.objects.get(id=categoria)
        evento = Evento.objects.create(usuario=valid_data['user'], categoria=categoriaObj, **request.data)
        return Response(EventoSerializer(evento).data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
def creato(request):

    requestData = request.data
    tok = requestData.pop('token', None)
    data = {'token': tok}
    valid_data = VerifyJSONWebTokenSerializer().validate(data)
    user = valid_data['user']
    #categoria = requestData.pop('categoria', None)
    categoriaObj = Categoria.objects.get(id=1)
    evento = Evento.objects.create(usuario=user, categoria=categoriaObj, **request.data)
    return Response(EventoSerializer(evento).data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
def deleteEvent(request):
    requestData = request.data['id']
    print(requestData)
    Evento.objects.filter(id=requestData).delete()
    return Response(status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def getCategories(request):
    catgorias = Categoria.objects.all()
    return HttpResponse(serialize("json", catgorias))

@csrf_exempt
@api_view(['GET'])
def getCategoriesById(request):
    catId = request.GET.get('id')
    categorias = Categoria.objects.get(id=catId)
    return Response(CategoriaSerializer(categorias).data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['GET'])
def getEventById(request):
    eventId = request.GET.get('eventId')
    evento = Evento.objects.get(id=eventId)
    return Response(CategoriaSerializer(evento).data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
def updateEvent(request):
    requestData = request.data
    print(requestData)
    evento = Evento.objects.get(id=requestData['id'])
    evento.nombre = requestData['nombre']
    categoriaObj = Categoria.objects.get(id=2)
    evento.categoria = categoriaObj

    evento.lugar = requestData['lugar']
    evento.direccion = requestData['direccion']
    evento.fechaInicio = requestData['fechaInicio']
    evento.fechaFin = requestData['fechaFin']
    evento.presencial = requestData['presencial']
    evento.save()
    return Response(EventoSerializer(evento).data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
def add_user_view(request):
    if request.method == 'POST':
        requestData = request.data
        username = requestData['username']
        password = requestData['password']
        user_model = User.objects.create_user(username=username, password=password)
        user_model.save()
    return Response(UsuarioSerializer(user_model).data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        requestData = request.data
        username = requestData['username']
        password = requestData['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = "ok"
        else:
            message = 'Nombre de usuario o contraseña incorrectos'

    return Response({"message": message})


@csrf_exempt
def index(request):
    eventoList = Evento.objects.all()
    if request.method == 'POST':
        jsonData = json.loads(request.body)
        data = {'token': jsonData['token']}

        try:
            valid_data = VerifyJSONWebTokenSerializer().validate(data)
        except ValidationError as e:
            pass
        else:
            if valid_data['user']:
                eventoList = Evento.objects.filter(usuario=valid_data['user'])
    return HttpResponse(serialize("json", eventoList))
