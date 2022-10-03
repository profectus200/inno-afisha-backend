from rest_framework import viewsets

from events.models import EventModel
from events.permissions import IsAdminOrReadOnly
from events.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAdminOrReadOnly, )