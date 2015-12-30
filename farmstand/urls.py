from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from saleor.cart.urls import urlpatterns as cart_urls
from saleor.checkout.urls import urlpatterns as checkout_urls
from saleor.core.sitemaps import sitemaps
from saleor.core.urls import urlpatterns as core_urls
from saleor.order.urls import urlpatterns as order_urls
from saleor.product.urls import urlpatterns as product_urls
from saleor.registration.urls import urlpatterns as registration_urls
from saleor.userprofile.urls import urlpatterns as userprofile_urls
from saleor.dashboard.urls import urlpatterns as dashboard_urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(registration_urls, namespace='registration')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^cart/', include(cart_urls, namespace='cart')),
    url(r'^checkout/', include(checkout_urls, namespace='checkout')),
    url(r'^dashboard/', include(dashboard_urls, namespace='dashboard')),
    url(r'^order/', include(order_urls, namespace='order')),
    url(r'^products/', include(product_urls, namespace='product')),
    url(r'^profile/', include(userprofile_urls, namespace='profile')),
    url(r'^selectable/', include('selectable.urls')),
    url(r'^store/', include('payments.urls')),
    url(r'^$', include(core_urls), name='home'),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT})
    )
