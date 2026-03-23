from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HeroSection, Food
from .serializers import HeroSerializer, FoodSerializer

@api_view(['GET'])
def hero_view(request):
    hero = HeroSection.objects.last()
    return Response(HeroSerializer(hero).data)

@api_view(['GET'])
def featured_foods(request):
    foods = Food.objects.filter(is_featured=True, is_available=True)
    return Response(FoodSerializer(foods, many=True).data)




from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CategoryMenu
from .serializers import CategoryMenuSerializer

class MenuAPIView(APIView):
    def get(self, request):
        categories = CategoryMenu.objects.all()
        serializer = CategoryMenuSerializer(categories, many=True, context={"request": request})
        return Response(serializer.data)




from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodMenu
from .serializers import FoodMenuSerializer

class FoodDetailAPIView(APIView):
    def get(self, request, id):
        try:
            food = FoodMenu.objects.get(id=id)
            serializer = FoodMenuSerializer(food)
            return Response(serializer.data)
        except FoodMenu.DoesNotExist:
            return Response({"error": "Food not found"}, status=404)