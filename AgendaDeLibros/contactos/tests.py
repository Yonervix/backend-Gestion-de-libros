from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contacto
from .serializers import contactoSerializer

@api_view(['GET'])
def lista_contactos(request):
    contactos = Contacto.objects.all()
    serializer = contactoSerializer(contactos, many=True)
    return Response(serializer.data)