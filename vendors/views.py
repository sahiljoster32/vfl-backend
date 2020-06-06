from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VendorViewSerializer, VendorCreateSerializer
from .models import Vendor
from django.http import Http404

# Create your views here.

class VendorView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = VendorViewSerializer

    def get_object(self, pk):
        try:
            vendor = Vendor.objects.filter(pk=pk)
            print(vendor[0])
            return vendor[0]
        except:
            raise Http404

    def get(self, request, pk):
        vendor = self.get_object(pk)
        serializer = self.get_serializer(vendor)

        return Response(serializer.data,status=status.HTTP_200_OK)

   
    def put(self,request,pk):
        pass
    def patch(self, request, pk):
        pass
    def delete(self,request,pk):
        pass

class VendorCreateView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = VendorCreateSerializer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
