from django.apps import AppConfig

class MapConfig(AppConfig):
    name = 'map'
    def ready(self):
        from map.models import AbstractTile, Problem
        AbstractTile.objects.all().delete()
