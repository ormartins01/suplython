from rest_framework import serializers
from .models import Supplier
from contracts.models import Contract
from rest_framework.validators import UniqueValidator
from .new_serializer import ContractNewSerializer, CategoryNewSerializer, DepartmentNewSerializer


class SupplierSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(Supplier.objects.all(), "Name should be unique.")]
    )

    email = serializers.EmailField(
        validators=[UniqueValidator(Supplier.objects.all(), "E-mail should be unique.")]
    )

    tel = serializers.CharField(
        validators=[
            UniqueValidator(Supplier.objects.all(), "Contact should be unique.")
        ]
    )

    class Meta:
        model = Supplier
        fields = [
            "id",
            "name",
            "email",
            "tel",
            "cnpj",
        ]

        read_only_fields = ["id"]

    def create(self, validated_data):
        return Supplier.objects.create(**validated_data)


class SupplierDetailSerializer(serializers.ModelSerializer):
    
    # contracts   = ContractNewSerializer(many=True)
    # categories   = CategoryNewSerializer(many=True)
    # departments = DepartmentNewSerializer(many=True)
    contract_id = serializers.IntegerField(write_only=True)


    class Meta:
        model = Supplier
        fields = ["id", "name", "email", "tel", "cnpj",  "contract_id"]

        read_only_fields = ["id", "name", "email", "tel", "cnpj"]

        # def update(self, instance: Supplier, validated_data):

        #     for key, value in validated_data.items():
        #         setattr(instance, key, value)

        #     instance.save()

        #     return instance
