from django.conf.urls import patterns, include, url
from first import views

urlpatterns = patterns('',
    
    url(r'^login/$', views.Login),
    url(r'^auth/$', views.AuthView),
    url(r'^logout/$', views.Logout),

    url(r'^home/$', views.Home, name='home'),
    url(r'^restaurants/$', views.RestaurantListView.as_view(), name='restaurant_list'),
    url(r'^restaurants/(?P<pk>[0-9]+)/$', views.RestaurantDetailView.as_view(), name='restaurant_detail'),

    url(r'^write_review/$', views.WriteReview.as_view(), name='write_review'),
    url(r'^write_review/(?P<pk>[0-9]+)/$', views.WriteReview.as_view(), name='write_review_restaurant'),
    url(r'^restaurants/(?P<pk>[0-9]+)/review/(?P<id>[0-9]+)/update/$', views.ReviewUpdateView.as_view(), name='update_review'),
    url(r'^restaurants/(?P<pk>[0-9]+)/review/(?P<id>[0-9]+)/delete/$', views.ReviewDeleteView.as_view(), name='delete_review'),

    url(r'^restaurants/(?P<pk>[0-9]+)/rate/$', views.Rate, name='rate'),
)
