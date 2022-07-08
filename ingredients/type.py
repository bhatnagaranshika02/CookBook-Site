from ingredients.models import Category, Ingredients
from graphene_django import DjangoObjectType

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'ingredients')

class IngredientsType(DjangoObjectType):
    class Meta:
        model = Ingredients
        field = ('id', 'name', 'notes', 'category')