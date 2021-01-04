from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import static
from plagapp import views
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView, name='index'),
    # url(r'^plagapp/', include('plagapp.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
