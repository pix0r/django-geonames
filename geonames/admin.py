from django.contrib.gis import admin

from geonames.models import Geoname

class GeonameAdmin(admin.OSMGeoAdmin):
    search_fields = ('name',)

admin.site.register(Geoname, GeonameAdmin)
