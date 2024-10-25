from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from .models import Event
from .serializers import EventCreateSerializer, EventSerializer


class EventApiView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = Event.objects.all().order_by("timestamp")
    serializer_class = EventSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return EventCreateSerializer
        return self.serializer_class

