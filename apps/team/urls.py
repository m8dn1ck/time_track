#
#import django
from django.urls import path

#
# local imports
from .views import team, add

app_name = 'team'

urlpatterns = [
    path('add/', add, name='add'),
    path('<int:team_id>/', team, name='team')
]






