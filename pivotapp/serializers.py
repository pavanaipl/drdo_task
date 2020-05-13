from rest_framework.serializers import ModelSerializer

from .models import *

class UsersDetailsSerializers(ModelSerializer):

    class Meta:
        model = UsersDetails
        exclude = ('active',)