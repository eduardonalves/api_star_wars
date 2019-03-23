from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from planets.models import Planet
import requests
import json

class PlanetSerializer(ModelSerializer):
	has_appeared = SerializerMethodField()
	class Meta:
		model = Planet

		fields = ('id', 'name', 'climate','terrain','has_appeared')

	def get_has_appeared(self, obj):
		url = 'https://swapi.co/api/planets/?format=json&search=%s' % (obj.name)
		response = requests.get(url)
		json_data = json.loads(response.text)
		i=0
		for results in json_data["results"]:
			all_films = results['films']
			for single_film in all_films:
				i = i + 1
		return i