from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'trydjango18.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'newsletter.views.home', name="home"),
    url(r'^contact/$', 'newsletter.views.contact', name="contact"),
    url(r'^admin/', include(admin.site.urls)),


]
+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

