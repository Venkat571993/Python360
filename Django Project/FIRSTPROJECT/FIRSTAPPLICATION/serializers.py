from rest_framework import serializers
from .models import CustomerDetail


class CustomerDetails_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields =['id','first_name','last_name','contact_number','City' ]