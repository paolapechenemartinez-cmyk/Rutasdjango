from django.http import HttpResponse

def bienvenido(request):

    return HttpResponse("hola desde las vistas de rutas")