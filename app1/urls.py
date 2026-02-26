from app1.views import drinkList, drinkDetail
from django.urls import path

urlpatterns = [
    path('drink-list/', drinkList, name='drink-list'),
    path('drink-list/<int:id>', drinkDetail, name='drink-detail'),
]
