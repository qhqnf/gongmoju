import os
import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .models import Ipo, SecurityCompany, IpoException
from .serializers import IpoSerializer, SecurityCompanySerializer, IpoExceptionSerializer

class IpoView(APIView):
    def get(self, request):
        qs = Ipo.objects.all()
        data = IpoSerializer(qs, many=True).data
        return Response(data)

    def post(self, request):
        bulk_data = request.data.get("data")
        locations = []
        for ipo in bulk_data:
            ipo_serializer = IpoSerializer(data=ipo)
            if ipo_serializer.is_valid():
                security_company_set = ipo_serializer.validated_data.pop("security_company_set")
                ipo_instance = ipo_serializer.save()
                for security_company in security_company_set:
                    security_company = SecurityCompany(ipo=ipo_instance, **security_company)
                    security_company.save()
                locations.append(f"{os.path.join(request.get_full_path(), str(ipo_instance.company_code))}")
            else:
                return Response(ipo_serializer.errors)
        return Response(locations)

class IpoRetrieveView(APIView):
    def get(self, request, company_code):
        qs = Ipo.objects.get(company_code=company_code)
        data = IpoSerializer(qs).data
        return Response(data)

    def put(self, request, company_code):
        data = request.data.get("data")
        del data["security_company_set"]
        ipo_instance = Ipo.objects.get(company_code=company_code)
        ipo_serializer = IpoSerializer(ipo_instance, data=data, partial=True)

        if ipo_serializer.is_valid():
            ipo_serializer.save()
            return Response(ipo_serializer.data)
        else:
            return Response(ipo_serializer.errors ,status=HTTP_400_BAD_REQUEST)

class IpoExceptionView(APIView):
    def get(self, request):
        qs = IpoException.objects.all()
        data = IpoExceptionSerializer(qs, many=True).data
        return Response(data)
