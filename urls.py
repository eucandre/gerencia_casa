from django.conf.urls.defaults import patterns, include, url
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gerencia_casa.views.home', name='home'),
    # url(r'^gerencia_casa/', include('gerencia_casa.foo.urls')),
    url(r'^$','app_casa.views.pagina_inicial'),
    url(r'^receitas/$','app_casa.views.receita_casa'),
    url(r'^despesas/$','app_casa.views.despesas_casa'),
    url(r'^em_caixa/$','app_casa.views.caixa'),
    # Uncomment the admin/doc line below to enable admin documentation:

    (r'^login/$',"django.contrib.auth.views.login",{"template_name":"login.html"}),
    (r'^logout/$',"django.contrib.auth.views.logout_then_login",{"login_url":"/"}),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }))
