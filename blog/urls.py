from django.urls import path

#from itg.urls import urlpatterns
from . import views

urlpatterns = [
    path("", views.get_all_blog),
    path("catalog/", views.catalog),
    path("catalog/<int:blog_id>/", views.get_blog_by_id),
    path("catalog/<slug:slug>/", views.get_category_by_name),
]