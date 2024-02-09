from rest_framework.filters import BaseFilterBackend
from django.db.models import Q


class SortFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        ordering = request.query_params.get("sort", None)
        if ordering:
            return queryset.order_by(ordering)
        return queryset



class SearchFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        search = request.query_params.get('search', None)
        if search:
            query = Q()
            for field in queryset.model._meta.fields:
                if field.name != 'id':
                    query |= Q(**{f'{field.name}__icontains': search})
            return queryset.filter(query)
        return queryset


