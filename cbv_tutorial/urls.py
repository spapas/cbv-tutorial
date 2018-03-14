from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


class HomeTemplateView(TemplateView):
    template_name ='home.html'


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', LoginView.as_view(), name='login', ),
    url(r'^accounts/logout/', LogoutView.as_view(), name='logout', ),

    url(r'^$', HomeTemplateView.as_view() ),
    url(r'^non-django-cbv/', include('core.urls')),
    url(r'^djangocbv/', include('djangocbv.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
