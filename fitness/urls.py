from rest_framework import routers

from fitness.views import WorkoutViewSet, MuscleGroupViewSet, ConditionViewSet, DisciplineViewSet

app_name = 'fitness'

router = routers.DefaultRouter()
router.register('workouts', WorkoutViewSet)
router.register('muscle-groups', MuscleGroupViewSet)
router.register('conditions', ConditionViewSet)
router.register('disciplines', DisciplineViewSet)
# router.register('goals', GoalViewSet)

urlpatterns = router.urls
