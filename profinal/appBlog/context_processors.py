from .models import *
import datetime
import random



def mostrarFecha(request):
    fecha = datetime.datetime.now() #relojito para el footer
    return {
        'fecha': fecha.date
    }
    
#-------------------------------------------------------------

def verAvatar(request):
    try:
        x = Avatar.objects.filter(user=request.user)
        if len(x)!=0:
            avatarsin=x[0].imagen.url
        else:
            avatarsin="../media/avatars/AvatarB.png"
    except:
        avatarsin="../media/avatars/AvatarB.png"
    return {
        'avatarsin' : avatarsin
    }
    
#-------------------------------------------------------------

def exhibPost(request):
    try:
        x= CrearPost.objects.all().order_by('-creado_el')#ver el mas reciente
        if len(x)!=0:
            titulito=x[0].titulo
            fotito=x[0].imagen.url
            autorcito=x[0].autor
            postin=x[0]
            idecito=postin.id
        else:
            titulito="No hay nada para mostrar"
            fotito="../media/ImagenPost/SinPost.png"
            autorcito="Sin creador"
            idecito=1
    except:
        titulito="No hay nada para mostrar"
        autorcito="Sin creador"
        fotito="../media/ImagenPost/SinPost.png"
        idecito=1
    return {
        'titulito':titulito,'fotito':fotito,"autorcito":autorcito,"idecito":idecito
    }
    
#-------------------------------------------------------------
def exhibPostAleatorio(request):
    try:
        x= CrearPost.objects.all()
        if len(x)!=0:
            postingo=random.choice(x)
            
            rtitulo=postingo.titulo
            rfoto=postingo.imagen.url
            rautor=postingo.autor
            rpostin=postingo.id
        else:
            rtitulo="No hay nada para mostrar"
            rfoto="../media/ImagenPost/SinPost.png"
            rautor="Sin creador"
            rpostin=""
    except:
        rtitulo="No hay nada para mostrar"
        rautor="Sin creador"
        rfoto="../media/ImagenPost/SinPost.png"
        rpostin=""
    return {
        'rtitulo':rtitulo,'rfoto':rfoto,"rautor":rautor,"rpostin":rpostin
    }
#-------------------------------------------------------------
def exhibPostAleatorioTriple(request):
    try:
        x= CrearPost.objects.all()
        if len(x)>=3:
            postines=random.sample(list(x),3)
            postingo1=postines[0]
            postingo2=postines[1]
            postingo3=postines[2]
            
            r1titulo=postingo1.titulo
            r1foto=postingo1.imagen.url
            r1autor=postingo1.autor
            r1postin=postingo1.id
            r1fechin=postingo1.creado_el
            
            r2titulo=postingo2.titulo
            r2foto=postingo2.imagen.url
            r2autor=postingo2.autor
            r2postin=postingo2.id
            r2fechin=postingo2.creado_el
            
            r3titulo=postingo3.titulo
            r3foto=postingo3.imagen.url
            r3autor=postingo3.autor
            r3postin=postingo3.id
            r3fechin=postingo3.creado_el
        
        elif len(x)>1 and len(x)<=2:
            
            postines=random.sample(list(x),2)
            postingo1=postines[0]
            postingo2=postines[1]
            
            r1titulo=postingo1.titulo
            r1foto=postingo1.imagen.url
            r1autor=postingo1.autor
            r1postin=postingo1.id
            r1fechin=postingo1.creado_el
            
            r2titulo=postingo2.titulo
            r2foto=postingo2.imagen.url
            r2autor=postingo2.autor
            r2postin=postingo2.id
            r2fechin=postingo2.creado_el
            
            r3titulo="No hay nada para mostrar"
            r3autor="Sin creador"
            r3foto="../media/ImagenPost/SinPost.png"
            r3postin=""
            r3fechin=""
            
        elif len(x)!=0:
            postingo1=x[0]
            r1titulo=postingo1.titulo
            r1foto=postingo1.imagen.url
            r1autor=postingo1.autor
            r1postin=postingo1.id
            r1fechin=postingo1.creado_el
            
            r2titulo="No hay nada para mostrar"
            r2autor="Sin creador"
            r2foto="../media/ImagenPost/SinPost.png"
            r2postin=""
            r2fechin=""
            
            r3titulo="No hay nada para mostrar"
            r3autor="Sin creador"
            r3foto="../media/ImagenPost/SinPost.png"
            r3postin=""
            r3fechin=""
            
        else:
            r1titulo="No hay nada para mostrar"
            r1autor="Sin creador"
            r1foto="../media/ImagenPost/SinPost.png"
            r1postin=""
            r1fechin=""
            
            r2titulo="No hay nada para mostrar"
            r2autor="Sin creador"
            r2foto="../media/ImagenPost/SinPost.png"
            r2postin=""
            r2fechin=""
            
            r3titulo="No hay nada para mostrar"
            r3autor="Sin creador"
            r3foto="../media/ImagenPost/SinPost.png"
            r3postin=""
            r3fechin=""
            
    except:
        r1titulo="No hay nada para mostrar"
        r1autor="Sin creador"
        r1foto="../media/ImagenPost/SinPost.png"
        r1postin=""
        r1fechin=""
        
        r2titulo="No hay nada para mostrar"
        r2autor="Sin creador"
        r2foto="../media/ImagenPost/SinPost.png"
        r2postin=""
        r2fechin=""
        
        r3titulo="No hay nada para mostrar"
        r3autor="Sin creador"
        r3foto="../media/ImagenPost/SinPost.png"
        r3postin=""
        r3fechin=""
    return {
        'r1titulo':r1titulo,'r1foto':r1foto,"r1autor":r1autor,"r1postin":r1postin,"r1fechin":r1fechin,'r2titulo':r2titulo,'r2foto':r2foto,"r2autor":r2autor,"r2postin":r2postin,"r2fechin":r2fechin,'r3titulo':r3titulo,'r3foto':r3foto,"r3autor":r3autor,"r3postin":r3postin,"r3fechin":r3fechin
    }
#------------------------------------------------------------------
