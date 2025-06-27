from rest_framework import viewsets 
from .serializers import loginSerializer
from .models import logi
class loginview(viewsets.ModelViewSet):
    queryset=login.objects.all()
    serializer_class=loginSerializer

