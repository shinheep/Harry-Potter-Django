#api/urls.py

from django.urls import path
from .views import schools
from .views import houses

urlpatterns = [
    path('schools/', schools.SchoolsView.as_view(), name='index'),
    path('schools/<int:id>/', schools.SchoolView.as_view(), name='School-Details'),
    path('houses/', houses.HousesView.as_view(), name='index'),
    path('houses/<int:id>/', houses.HouseView.as_view(), name='House-Details')
]