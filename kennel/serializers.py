from rest_framework import serializers
from .models import Kennel

class KennelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kennel
        fields = ('id', 'code', 'manager', 'guest_can_pause', 'guest_can_skip')