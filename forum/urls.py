

from django.urls import path, include
from forum import views
urlpatterns = [
    path('forum/', views.ShowDataAll, name='ShowDataAllForum')
]
