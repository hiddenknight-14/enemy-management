from django.urls import path
from . import views

urlpatterns = [
    path('addEnemy/', views.addEnemy, name='addEnemy'),
    path('mark_as_revenge_taken/<int:pk>/', views.mark_as_revenge_taken, name='mark_as_revenge_taken'),
    path('mark_as_revenge_not_taken/<int:pk>/', views.mark_as_revenge_not_taken, name='mark_as_revenge_not_taken'),
    path('deleteEnemy/<int:pk>', views.deleteEnemy, name='deleteEnemy'),
    path('editEnemy/<int:pk>/', views.editEnemy, name='editEnemy'),
]