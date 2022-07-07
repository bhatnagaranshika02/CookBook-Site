from ingredients.type import CategoryType, IngredientsType
from ingredients.models import Category, Ingredients
import graphene

class Query(graphene.Object_Type):
    all_ingredients = graphene.List()
    all_categories = graphene.Field(required=True, name=String(), id=ID())

    def resolve_all_ingredients(self, info):
        return Ingredients.objects.select_related("Category").all()
