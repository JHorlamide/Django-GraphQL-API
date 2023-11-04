from django.urls import path
from strawberry.django.views import GraphQLView
from .schema import schema
from . import views

urlpatterns = [
    path("graphql", GraphQLView.as_view(schema=schema)),
]