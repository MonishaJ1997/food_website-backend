from django.db import models

class HeroSection(models.Model):
    tag = models.CharField(max_length=50, default="Hungry?")
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    main_image = models.ImageField(upload_to='hero/')
    button_primary = models.CharField(max_length=50, default="Order Now")
    button_secondary = models.CharField(max_length=50, default="Explore More")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='foods/')
    is_featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    


from django.db import models

class CategoryMenu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    categoryMenu = models.ForeignKey(
        CategoryMenu,
        on_delete=models.CASCADE,
        related_name="subcategories"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.categoryMenu.name} - {self.name}"


class FoodMenu(models.Model):
    categoryMenu = models.ForeignKey(CategoryMenu, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name="foods"
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="foods/")

    def __str__(self):
        return self.name