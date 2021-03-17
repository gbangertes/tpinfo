from .models import Noticia
import django_filters
from django.forms.widgets import SelectDateWidget


class FiltroBusqueda(django_filters.FilterSet):
    created_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'dd/mm/aaaa'}))

    class Meta:
        model = Noticia
        fields = ['autor', 'categoria', 'created_date', ]
