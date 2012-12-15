from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'(\d+)$', 'keuken.views.details', name='recipe-details'),
)