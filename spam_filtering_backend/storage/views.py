from rest_framework import viewsets
from .models import Mails
from .serializers import MailsSerializer


class MailViewSet(viewsets.ModelViewSet):
    queryset = Mails.objects.all()
    serializer_class = MailsSerializer
