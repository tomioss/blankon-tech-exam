from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny

from .models import Event
from .serializers import EventSerializer


class EventApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [AllowAny,]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

