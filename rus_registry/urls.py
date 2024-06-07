from django.urls import path

from rus_registry.apps import RusRegistryConfig
from rus_registry.views import RusRegistryServerView

app_name = RusRegistryConfig.name


urlpatterns = [
    path('rus_registry/', RusRegistryServerView.as_view(), name='rus_registry'),
]
