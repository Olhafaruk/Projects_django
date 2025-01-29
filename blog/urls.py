from django.urls import path

#from itg.urls import urlpatterns
from . import views

urlpatterns = [
    path("", views.get_all_blog),
    path("catalog/", views.catalog, name="catalog"),
    path("catalog/<int:article_id>/", views.get_detail_article_by_id, name="detail_article_by_id"),
    path("catalog/<slug:slug>/", views.get_category_by_name),
]