from ingredients.models import Category, Ingredients
from graphene_django import DjangoObjectModel

class CategoryType(DjangoObjectModel):
    class Meta:
        model = Category
        fields = ('id', 'name', 'ingredients')

class IngredientsType(DjangoObjectModel):
    class Meta:
        model = Ingredients
        field = ('id', 'name', 'notes', 'category')