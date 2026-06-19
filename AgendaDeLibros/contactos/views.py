from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Libro
from .serializers import LibroSerializer, LibroSerializerReg , LibroSerializerUpdate
from drf_yasg.utils import swagger_auto_schema
from django.core.paginator import Paginator


@swagger_auto_schema(
    method='get',
    operation_description='Lista todos los libros.',
    responses={200: 'Exitoso'}
)


@api_view(['GET'])
def lista_libros(request):

    page = request.GET.get('page', 1)

    libros = Libro.objects.all()

    paginator = Paginator(libros, 3)  # 3 libros por página

    page_obj = paginator.get_page(page)

    serializer = LibroSerializer(page_obj, many=True)

    return Response({
        'pagina_actual': page_obj.number,
        'total_paginas': paginator.num_pages,
        'libros': serializer.data
    })

@swagger_auto_schema(
    method='post',
    operation_description='Añade un nuevo libro.',
    request_body=LibroSerializerReg,
    responses={200: 'Exitoso', 400: 'Error'}
)

@api_view(['POST'])
def crear_libro(request):
    titulo = request.data.get('titulo')
    autor = request.data.get('autor')
    precio = request.data.get('precio')
    fecha_publicacion = request.data.get('fecha_publicacion')

    if not titulo or not autor or not precio or not fecha_publicacion:
        return Response({'error': 'Faltan campos requeridos'}, status=400)

    serialData = LibroSerializerReg(data=request.data)

    if serialData.is_valid():
        serialData.save()
    else:
        return Response(serialData.errors, status=400)

    return Response({'message': 'Libro creado exitosamente'}, status=201)

@swagger_auto_schema(
    method='put',
    operation_description='Actualiza un libro.',
    request_body=LibroSerializerUpdate,
    responses={200: 'Exitoso', 400: 'Error'}
)

@api_view(['PUT'])
def actualizar_libro(request):
    pk = request.data.get('id')
    print(pk)

    titulo = request.data.get('titulo')
    autor = request.data.get('autor')
    precio = request.data.get('precio')
    fecha_publicacion = request.data.get('fecha_publicacion')

    if not titulo or not autor or not precio or not fecha_publicacion:
        return Response({'error': 'Faltan campos requeridos'}, status=400)

    try:
        libro_instance = Libro.objects.get(id=pk)
    except Libro.DoesNotExist:
        return Response({'error': 'Libro no encontrado'}, status=404)

    serialData = LibroSerializerUpdate(
        instance=libro_instance,
        data=request.data
    )

    if serialData.is_valid():
        serialData.save()
    else:
        return Response(serialData.errors, status=400)

    return Response(
        {'message': 'Libro actualizado exitosamente'},
        status=200
    )

@swagger_auto_schema(
    method='delete',
    operation_description='Elimina un libro por ID.',
    responses={200: 'Exitoso', 404: 'No encontrado'}
)


@api_view(['DELETE'])
def eliminar_libro(request, id):
    try:
        libro_instance = Libro.objects.get(id=id)
    except Libro.DoesNotExist:
        return Response({'error': 'Libro no encontrado'}, status=404)

    libro_instance.delete()
    return Response({'message': 'Libro eliminado exitosamente'}, status=200)