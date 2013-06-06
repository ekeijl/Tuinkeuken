from django.conf.urls import patterns, url

urlpatterns = patterns('keuken.views',

    url(r'^$', 'index'),
    url(r'(?P<id>\d+)$', 'detail', name='detail'),
    url(r'(?P<author>\w+)$', 'list_by_author', name='recipes-by-author'),
)
