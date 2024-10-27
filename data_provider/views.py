from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from data_provider.filters import EventFilter
from data_provider.models import Event
from data_provider.serializers import EventCreateSerializer, EventSerializer


class EventApiView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = Event.objects.all().order_by("timestamp")
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventFilter

    def get_serializer_class(self):
        if self.action == "create":
            return EventCreateSerializer
        return self.serializer_class

