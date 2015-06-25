from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover()

class SimpleStaticView(TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template_name') + ".html"]

    def get(self, request, *args, **kwargs):
        from django.contrib.auth import authenticate, login
        if request.user.is_anonymous():
            # Auto-login the User for Demonstration Purposes
            user = authenticate()
            login(request, user)
        return super(SimpleStaticView, self).get(request, *args, **kwargs)

urlpatterns = [
    # url(r'^', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^articles/', include('articles.urls', namespace='articles')),
    url(r'^$', TemplateView.as_view(template_name='articles/index.html')),
]


urlpatterns = format_suffix_patterns(urlpatterns)

# urlpatterns = patterns('',
#     # Examples:
#     url(r'^$', 'articles.views.index', name='home'),
#    url(r'^', include(router.urls)),
#     url(r'^profile/', include('profiles.urls', namespace='profile')),
#     url(r'^authentication/', include('authentication.urls', namespace='authentication')),
#
#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# )
