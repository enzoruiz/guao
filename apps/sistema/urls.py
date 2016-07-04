from django.conf.urls import include, url
from .views import PublishView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^publish/$', login_required(PublishView.as_view()), name="publish"),
    url(r'^publish/([0-9]+)/$', login_required(PublishView.as_view()), name="publish_edit"),
]