from django.urls import include, path
from rest_framework_nested import routers
from repetory.views import RepertoryView
router = routers.SimpleRouter(trailing_slash=False)

router.register('repertory', RepertoryView, basename='repertory')

urlpatterns = [
    path('', include(router.urls)),
]
