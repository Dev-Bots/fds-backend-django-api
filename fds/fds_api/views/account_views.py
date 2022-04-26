from rest_framework import generics, permissions, viewsets


from ..permissions import *
from ..models import Player, Club, Scout
from ..serializers import PlayerSerializer, ClubSerializer, ScoutSerializer


# Create your views here.

class Players(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    # permission_classes = [IsOwnerOrReadOnly]
    
    
   
class Clubs(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    

class Scouts(viewsets.ModelViewSet):
    queryset = Scout.objects.all()
    serializer_class = ScoutSerializer   
    #permission_classes = [IsClubOrScoutEditRetrive]

    #this is for the depth of the nested returned json
    def get_serializer_class(self):
        if self.request.method == "GET":
            self.serializer_class.Meta.depth = 1
        else:
            self.serializer_class.Meta.depth = 0
        return self.serializer_class
    

""" VIEWSET ACTIONS

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
"""


""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""


