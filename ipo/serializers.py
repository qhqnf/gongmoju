from rest_framework import serializers
from rest_framework.serializers import StringRelatedField
from .models import Ipo, SecurityCompany, IpoException

class SecurityCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityCompany
        fields = (
            "company_name",
            "stock_amount",
        )

class IpoSerializer(serializers.ModelSerializer):
    security_company_set = SecurityCompanySerializer(many=True)

    class Meta:
        model = Ipo
        fields = "__all__"
        read_only_fields = ("security_company_set",)

class IpoExceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpoException
        exclude = ["id"]