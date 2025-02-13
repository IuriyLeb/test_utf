from django.urls import path
from .views import FoodCategoryListView

urlpatterns = [
    path('api/v1/foods/', FoodCategoryListView.as_view(), name='food-category-list'),
]
