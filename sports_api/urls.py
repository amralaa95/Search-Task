from django.conf.urls import url

from .views import SearchResultView

urlpatterns = [
    url(r'^sports_search/$', SearchResultView.as_view(), name='sports_api'),
]