
from django.urls import path, include
# from .views import Clubs, Players, Scouts, Events, EventActions, SkillView, ParameterView, GradeView, Results
from rest_framework.routers import DefaultRouter

app_name = 'fds_api'

router = DefaultRouter()
# router.register(r'players', Players, basename="players")
# router.register(r'clubs', Clubs, basename="clubs")
# router.register(r'scouts', Scouts, basename="scouts")

# router.register(r'events', Events, basename='events')
# router.register(r'event_actions', EventActions, basename='eventactions')

# router.register(r'skills', SkillView, basename='skill')
# router.register(r'parameters', ParameterView, basename='parameters')
# router.register(r'grade', GradeView, basename='grade' )
# router.register(r'results', Results, basename='results')

urlpatterns = [
    path('', include(router.urls)),
   #you can add other paths here
]

