from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', login_required(views.IdeaListView.as_view()), name="idealist"),
   url(r'^secrets/$', login_required(views.SecretView.as_view()), name="secret"),
]
