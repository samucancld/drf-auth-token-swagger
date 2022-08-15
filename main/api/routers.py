from rest_framework import routers
from .viewsets import RecipeViewSet, TagViewSet

router = routers.DefaultRouter(
    # trailing_slash = False
)

router.register(
    prefix = "recipes",
    viewset = RecipeViewSet,
    basename="recipes",
)
router.register(
    prefix="tags",
    viewset = TagViewSet,
    basename = "tags",
)

urlpatterns = router.urls

for url in urlpatterns:
    print(f"{url}\n")