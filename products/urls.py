from django.conf.urls import url, include
from .views import all_products, new, cactus, animals, flamingos, palm, pink, deer

urlpatterns = [
    url(r'^$', all_products, name="products"),
    url(r'^new/$', new, name="new"),
    url(r'^cactus/$', cactus, name="cactus"),
    url(r'^animals/$', animals, name="animals"),
    url(r'^flamingos/$', flamingos, name="flamingos"),
    url(r'^palm/$', palm, name="palmtrees"),
    url(r'^pink/$', pink, name="pink"),
    url(r'^deer/$', deer, name="deer"),
    ]