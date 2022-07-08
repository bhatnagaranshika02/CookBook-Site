from ingredients.type import CategoryType, IngredientsType
from ingredients.models import Category, Ingredients
import graphene

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientsType)
    all_categories = graphene.Field(CategoryType, name=graphene.String(), id=graphene.ID())

    def resolve_all_ingredients(self, info):
        return Ingredients.objects.select_related("category").all()

    def resolve_all_categories(self, info, name=None, id=None):
        try:

            if name:
                return Category.objects.get(name=name)
            if id:
                return Category.objects.get(id=id)
        except Category.DoesNotExist:
            return None

class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    
    category = graphene.Field(CategoryType)
    erorr = graphene.String()
    success = graphene.Boolean()

    def mutate(self,info, name):
        if Category.objects.filter(name=name).exists():
            return CreateCategory(erorr="Already exists!")
        else:
            new_category = Category(
                name=name
            )
            new_category.save()
            return CreateCategory(category=new_category, success=True)

class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()

schema = graphene.Schema(query=Query, mutation = Mutation)
