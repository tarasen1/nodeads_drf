from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Group, Element
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import GroupSerializer, ElementSerializer

def index(request):
    return HttpResponse("Howdie")

class GroupView(APIView):
    def get_object(self, id):
        try:
            return Group.objects.get(id=id)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, id=None, format=None):
        print('hello', id)
        if id is not None:
                groups = self.get_object(id)
                serializer = GroupSerializer(groups)
        else:
                groups = Group.objects.all()
                serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)


class ElementView(APIView):
    def post(self, request, format=None):
        serializer = ElementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
