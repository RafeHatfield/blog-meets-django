from django.views.generic import ListView
from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from blogengine.models import Post, Category
from blogengine.views import PostsFeed

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

post_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'pub_date',
}

category_dict = {
    'queryset': Category.objects.all(),
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'blog': GenericSitemap(post_dict, priority=0.6),
    'category': GenericSitemap(category_dict, priority=0.6),
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog_meets_django.views.home', name='home'),
    # url(r'^blog_meets_django/', include('blog_meets_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Home page
    url(r'^$', 'blogengine.views.getPosts'),
    url(r'^(?P<selected_page>\d+)/?$', 'blogengine.views.getPosts'),

    url(r'^search/?$', 'blogengine.views.googlesearch'),

    # Blog posts
    url(r'^\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getPost'),

    # Categories
    url(r'^categories/?$', ListView.as_view(model=Category,)),
    url(r'^categories/(?P<categorySlug>\w+)/?$', 'blogengine.views.getCategory'),
    url(r'^categories/(?P<categorySlug>\w+)/(?P<selected_page>\d+)/?$', 'blogengine.views.getCategory'),

    # RSS feeds
    url(r'^feeds/posts/$', PostsFeed()),

    # the sitemap
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Flat pages
    url(r'', include('django.contrib.flatpages.urls')),
)
