from django.contrib.gis import admin

from geonames.models import Geoname, Alternate

from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter


class CityListFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('is topographically')
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'topo'

    def lookups(self, request, model_admin):
        return (
            ('city', _('city or town')),
            ('country', _('country')),
            ('continent', _('continent')),
        )

    def queryset(self, request, queryset):
        selected = self.value()
        if selected == 'city':
            queryset = queryset.filter(fcode='PPL')
        elif selected == 'country':
            queryset = queryset.filter(fcode='PCLI')
        elif selected == 'continent':
            queryset = queryset.filter(fcode='CONT')
        return queryset


class AlternateInline(admin.TabularInline):
    model = Alternate


class GeonameAdmin(admin.GeoModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'country', 'timezone')
    list_filter = (CityListFilter, 'country', 'timezone')
    inlines = (AlternateInline,)

admin.site.register(Geoname, GeonameAdmin)
