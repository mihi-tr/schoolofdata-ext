from django.conf.urls import patterns, include, url
import scodaext.apps.courses.views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'scodaquiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'scodaext.apps.courses.views.start'),
    url(r'^module/(?P<module>[-\w]+)/edit/$',
        'scodaext.apps.courses.views.editmodule'),
    url(r'^(?P<course>[-\w]+)/edit/$',
        'scodaext.apps.courses.views.editcourse'),
    url(r'^(?P<course>[-\w]+)/feature/$',
        'scodaext.apps.courses.views.featurecourse'),
    url(r'^(?P<course>[-\w]+)/edit/modules/$',
        'scodaext.apps.courses.views.editcoursemodule'),
    url(r'^create/$',
        'scodaext.apps.courses.views.createcourse'),
    url(r'^module/create/$',
        'scodaext.apps.courses.views.createmodule'),
    url(r'^module/(?P<module>[-\w]+)/$',
        'scodaext.apps.courses.views.moduleview'),
    url(r'^tag/(?P<tag>[-\w:]+)/$',
        'scodaext.apps.courses.views.tagview'),
    url(r'^(?P<course>[-\w]+)/$', 
        'scodaext.apps.courses.views.courseview'),
    url(r'^(?P<course>[-\w]+)/(?P<module>[-\w]+)/$',
        'scodaext.apps.courses.views.moduleview'),

)
