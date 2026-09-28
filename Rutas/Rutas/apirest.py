from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def mensaje(request):

    return Response({
        "mensaje": "Bienvenido a la API de rutas."
    })

@api_view(['POST'])
def guardar(request):

    datos = request.data

    return Response({
        'datos_recibidos': datos,
        'mensaje': 'datos guardados'
    })