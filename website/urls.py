from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.map_view, name="home"),
    #path('add', views.add, name="add"),
    path('veterans', views.veterans, name="veterans"),
    path("search/", SearchResultsView.as_view(), name="search"),
    path('map/', views.map_view, name='map'),
]