from django.db.models import Prefetch, Exists, OuterRef
from rest_framework.generics import ListAPIView

from .models import FoodCategory, Food, FoodListSerializer


class FoodCategoryListView(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):

        published_foods_qs = Food.objects.filter(is_publish=True)

        categories = (
            FoodCategory.objects.annotate(
                has_published_foods=Exists(
                    Food.objects.filter(category=OuterRef("pk"), is_publish=True)
                )
            )
            .filter(has_published_foods=True)
            .prefetch_related(Prefetch("food", queryset=published_foods_qs))
        )

        return categories
