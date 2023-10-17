### resources app urls


from django.urls import path
from . import views

app_name="resources"

urlpatterns=[
    #   pass a category in
    path('<slug:category_slug>/', views.list, name="resources_by_category"),
    #   pass nothing
    path('', views.list, name="resources"),
]