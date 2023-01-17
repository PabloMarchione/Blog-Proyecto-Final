from .models import CrearMensaje



def contadorMensajes(request):
    try:
        l1= CrearMensaje.objects.filter(receptor=request.user)
        l2= CrearMensaje.objects.filter(creador=request.user)
        contEntrada=len(l1)
        contSalida=len(l2)
    except:
        contEntrada= 0
        contSalida= 0
    
    return {
        "contEntrada":contEntrada,"contSalida":contSalida
    }