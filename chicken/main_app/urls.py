from django.urls import path
from . import views 

urlpatterns = [
  path('', views.home, name='home'),
  path('chickens/', views.chicken_index, name='chicken-index'),
  path('chickens/<int:chicken_id>/', views.chicken_detail, name='chicken-detail'),
  path('chickens/create/', views.ChickenCreate.as_view(), name='chicken-create'),
  path('chicken/<int:pk>/update/', views.ChickenUpdate.as_view(), name='chicken-update'),
  path('chicken/<int:pk>/delete/', views.ChickenDelete.as_view(), name='chicken-delete'),
  path(
        'chicken/<int:chicken_id>/add-eggs/', 
        views.add_eggs, 
        name='add-eggs'
    ),

]

