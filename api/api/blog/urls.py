from rest_framework_extensions.routers import ExtendedDefaultRouter
from . import views


router = ExtendedDefaultRouter()

router.register(r'posts', views.PostViewSet, base_name='post')
router.register(r'schema', views.PostSchemaViewSet, base_name='post-schema')
router.register(r'tags', views.TagViewSet, base_name='tag') \
      .register(r'posts', views.PostViewSet, base_name='tag-post',
                parents_query_lookups=['tag__title'])

urlpatterns = router.urls
