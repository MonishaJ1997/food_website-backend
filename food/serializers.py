from rest_framework import serializers
from .models import HeroSection, Food

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'




from rest_framework import serializers
from .models import CategoryMenu, SubCategory, FoodMenu

class FoodMenuSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = FoodMenu
        fields = ["id", "name", "price", "image", "description"]  # ✅ ADD THIS

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None


class SubCategorySerializer(serializers.ModelSerializer):
    foods = FoodMenuSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ["id", "name", "foods"]


class CategoryMenuSerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = CategoryMenu
        fields = ["id", "name", "subcategories"]