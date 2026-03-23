from django.urls import path
from .views import hero_view, featured_foods
from .views import MenuAPIView , FoodDetailAPIView

urlpatterns = [
    path('hero/', hero_view),
    path('foods/', featured_foods),

    path("menu/", MenuAPIView.as_view(), name="menu-api"),
    path("food/<int:id>/", FoodDetailAPIView.as_view(), name="food-detail"),
]
