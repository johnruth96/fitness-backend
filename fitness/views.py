import json
from json import JSONDecodeError

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from fitness.models import Workout, MuscleGroup, Discipline, Condition
from fitness.serializers import MuscleGroupSerializer, WorkoutSerializer, DisciplineSerializer, ConditionSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000


class WorkoutViewSet(viewsets.ModelViewSet):
    model = Workout
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def filter_queryset(self, queryset):
        """
        Filter with the Material UI DataGrid GridFilterModel
        """

        def apply_filter(queryset, field: str, operator: str, value):
            OPERATOR_LOOKUP_MAP = {
                'contains': 'contains',
                'equals': 'exact',
                'startsWith': 'startswith',
                'endsWith': 'endswith',
                'isAnyOf': 'in',
                'is': 'exact',
                'after': 'gt',
                'onOrAfter': 'gte',
                'before': 'lt',
                'onOrBefore': 'lte',
            }

            if operator == "isEmpty":
                return queryset.filter(**{f"{field}__isnull": True})

            if operator == "isNotEmpty":
                return queryset.filter(**{f"{field}__isnull": False})

            if operator == "not":
                return queryset.exclude(**{field: value})

            if operator in OPERATOR_LOOKUP_MAP:
                lookup = OPERATOR_LOOKUP_MAP[operator]
                return queryset.filter(**{f"{field}__{lookup}": value})

        filter_model_str = self.request.query_params.get("filterModel")
        if filter_model_str:
            try:
                filter_model = json.loads(filter_model_str)

                for item in filter_model["items"]:
                    queryset = apply_filter(queryset, item["field"], item["operator"], item["value"])
            except (JSONDecodeError, KeyError):
                pass

        return queryset

    @action(methods=["GET"], detail=False)
    def dates(self, request, pk=None):
        qs = Workout.objects.all()
        dates = qs.values_list("date", flat=True)
        dates = [date.strftime("%Y-%m-%d") for date in dates]
        return Response(dates)


class MuscleGroupViewSet(viewsets.ModelViewSet):
    model = MuscleGroup
    serializer_class = MuscleGroupSerializer
    queryset = MuscleGroup.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class ConditionViewSet(viewsets.ModelViewSet):
    model = Condition
    serializer_class = ConditionSerializer
    queryset = Condition.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class DisciplineViewSet(viewsets.ModelViewSet):
    model = Discipline
    serializer_class = DisciplineSerializer
    queryset = Discipline.objects.all()
    permission_classes = [permissions.IsAuthenticated]

# class GoalViewSet(viewsets.ModelViewSet):
#     model = Goal
#     serializer_class = GoalSerializer
#     queryset = Goal.objects.all()
#     permission_classes = [permissions.IsAuthenticated]
