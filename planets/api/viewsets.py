from rest_framework.viewsets import ModelViewSet
from planets.models import Planet
from .serializers import PlanetSerializer

class PlanetViewSet(ModelViewSet):
	serializer_class = PlanetSerializer

	def get_queryset(self):

		id = self.request.query_params.get('id', None)
		name = self.request.query_params.get('name', None)
		queryset = Planet.objects.all()

		if id:
			queryset = Planet.objects.filter(pk=id)

		if name:
			queryset = Planet.objects.filter(name__icontains=name)

		return queryset


