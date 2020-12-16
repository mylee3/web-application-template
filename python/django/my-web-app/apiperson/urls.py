from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /apipersons/api/v1/persons
    path('api/v1/persons', views.persons, name='list_persons'),
    path('api/v1/persons/<int:person_id>', views.get_person, name='get_person'),
    path('api/v1/persons/<int:person_id>/update', views.update_person, name='update_person'),
    path('api/v1/persons/create', views.create_person, name='create_person'),
]