from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from favourites.models import FavouriteModel
from favourites.serializers import FavouriteSerializer


class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = FavouriteModel.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user',)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset