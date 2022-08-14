from rest_framework import routers

from .viewsets import RecipeViewSet

router = routers.DefaultRouter()

router.register(
    prefix = "recipes",
    viewset = RecipeViewSet,
    basename="recipes",
)

urlpatterns = router.urls

# for url in urlpatterns:
#     print(f"{url}\n")