from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile, about, shipping, contact, stockists, returns
from accounts import url_reset

urlpatterns = [
    
    url(r'^index/$', index, name="index"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^about/$', about, name="about"),
    url(r'^shipping/$', shipping, name="shipping"),
    url(r'^contact/$', contact, name="contact"),
    url(r'^stockists/$', stockists, name="stockists"),
    url(r'^returns/$', returns, name="returns"),
]