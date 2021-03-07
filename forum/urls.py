

from django.urls import path, include
from forum import views
urlpatterns = [
    path('forum/', views.ShowDataAll, name='ShowDataAllForum'),
    path('forum/create', views.CreateData, name='CreateData'),
    path('forum/<int:id>', views.ShowDetailData, name='ShowDetailData'),
    path('forum/edit/<int:pk>', views.EditData, name="EditData"),
    path('forum/delete/<int:pk>', views.DeleteData, name="DeleteData")
]
