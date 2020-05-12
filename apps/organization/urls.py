from django.conf.urls import url
from apps.organization.views import OrgView

urlpatterns = [
    url(r'^list/',OrgView.as_view(),name='list'),
]