from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from core import views
from rest_framework.authtoken.views import ObtainAuthToken

from core.views import EventsView

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('eventos/<int:idUser>/', EventsView.as_view(), name="get events"),
    path('createEvent/', EventsView.as_view(), name="create events"),
    path('deleteEvent/', views.deleteEvent, name="delete events"),
    path('updateEvent/', views.updateEvent, name="update events"),
    path('createUser/', views.add_user_view, name="create user"),
    path('eventos/', views.index, name="create user"),
    path('login/', views.login_view, name="login user"),
    path('creato/', views.creato, name="crea user"),
    path('categories/', views.getCategories, name="crea user"),
    path('category/', views.getCategoriesById, name="crea user"),
    url(r'^eventById$', views.getEventById, name='verproducto'),
]
