from rest_framework.filters import BaseFilterBackend


class AlertTypeFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset
