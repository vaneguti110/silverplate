from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^crawl/', include('crawler.urls', namespace='crawl')),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home')
]
