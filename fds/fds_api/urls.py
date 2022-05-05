
from django.urls import path, include
from .views import Clubs, Players, Scouts, Events, EventActions, SkillView, ParameterView, GradeView, Results, QuestionView, AnswerView, CheckTeamBuilder, BuildTeams, TeamView, MakeMatch, MatchView, DataFill
from rest_framework.routers import DefaultRouter

app_name = 'fds_api'

router = DefaultRouter()
router.register(r'players', Players, basename="players")
router.register(r'clubs', Clubs, basename="clubs")
router.register(r'scouts', Scouts, basename="scouts")

router.register(r'events', Events, basename='events')
router.register(r'event_actions', EventActions, basename='eventactions')

router.register(r'skills', SkillView, basename='skill')
router.register(r'parameters', ParameterView, basename='parameters')
router.register(r'grade', GradeView, basename='grade' )
router.register(r'results', Results, basename='results')

router.register(r'questions', QuestionView, basename='questions' )
router.register(r'answers', AnswerView, basename='answers')

router.register(r'check_formation', CheckTeamBuilder, basename='check_formation')
router.register(r'build_teams', BuildTeams, basename='build_team')
router.register(r'view_teams', TeamView, basename='view_team')

router.register(r'make_match', MakeMatch, basename='make_match')
router.register(r'view_match', MatchView, basename='view_match')



router.register(r'data_fill', DataFill, basename='datafill')


urlpatterns = [
    path('', include(router.urls)),
   #you can add other paths here
]

