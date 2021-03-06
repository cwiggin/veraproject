from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import zinnia

urlpatterns = patterns('',
    
     url(r'^$', 'veraproject.views.home', name='home'),
     url(r'^shows/$', 'veraproject.views.shows', name='shows'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

url(r'^weblog/', include('zinnia.urls')),
url(r'^comments/', include('django.contrib.comments.urls')),

url(r'^', include('zinnia.urls.capabilities')),
url(r'^search/', include('zinnia.urls.search')),
url(r'^sitemap/', include('zinnia.urls.sitemap')),
url(r'^trackback/', include('zinnia.urls.trackback')),
url(r'^blog/tags/', include('zinnia.urls.tags')),
url(r'^blog/feeds/', include('zinnia.urls.feeds')),
url(r'^blog/random/', include('zinnia.urls.random')),
url(r'^blog/authors/', include('zinnia.urls.authors')),
url(r'^blog/categories/', include('zinnia.urls.categories')),
url(r'^blog/comments/', include('zinnia.urls.comments')),
url(r'^blog/', include('zinnia.urls.entries')),
url(r'^blog/', include('zinnia.urls.archives')),
url(r'^blog/', include('zinnia.urls.shortlink')),
url(r'^blog/', include('zinnia.urls.quick_entry')),