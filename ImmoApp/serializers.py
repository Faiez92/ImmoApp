from rest_framework import serializers
from ImmoApp.models.models import Appartement

class AppartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appartement
        fields = '__all__'
