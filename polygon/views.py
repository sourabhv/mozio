from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point, Polygon, GEOSGeometry

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Area
from .serializers import ProviderSerializer, AreaSerializer

User = get_user_model()

@api_view(['GET', 'POST'])
def provider_list(request):
    '''List all providers or create a new provider'''
    if request.method == 'GET':
        providers = User.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def provider_detail(request, provider_id):
    '''Read, update or delete a provider'''
    try:
        provider = User.objects.get(pk=provider_id)
    except User.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    print('GOT PROVIDER ' + provider.email)

    if request.method == 'GET':
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProviderSerializer(provider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def provider_area_list(request, provider_id):
    '''List all providers or create a new provider'''
    try:
        provider = User.objects.get(pk=provider_id)
    except User.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AreaSerializer(provider.areas.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def provider_area_detail(request, provider_id, area_id):
    try:
        provider = User.objects.get(pk=provider_id)
    except User.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    try:
        area = provider.areas.get(pk=area_id)
    except Area.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AreaSerializer(area)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AreaSerializer(area, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        area.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def provider_area_query(request, provider_id):
    try:
        provider = User.objects.get(pk=provider_id)
    except User.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    lat, lon = request.GET.get('lat', ''), request.GET.get('lon', '')
    if lat == '' or lon == '':
        return Response(status=HTTP_400_BAD_REQUEST)
    try:
        point = Point(float(lat), float(lon))
    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    areas = provider.areas.get(polygon__contains=point)
    serializer = AreaSerializer(areas)
    return Response(serializer.data)


def area_list(request):
    pass


def area_detail(request, area_id):
    pass


def area_query(request):
    lat, lon = request.GET.get('lat', ''), request.GET.get('lon', '')
    if lat == '' or lon == '':
        return Response(status=HTTP_400_BAD_REQUEST)
    try:
        point = Point(float(lat), float(lon))
    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    areas = Area.objects.get(polygon__contains=point)
    serializer = AreaSerializer(areas)
    return Response(serializer.data)
