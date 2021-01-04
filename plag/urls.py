from django.urls import path
from django.contrib.staticfiles.urls import static
from plagapp import views
from . import settings
urlpatterns = [
    path('', views.IndexView, name='index'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)