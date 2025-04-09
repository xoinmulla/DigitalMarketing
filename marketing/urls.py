from django.urls import path
from .views import home, campaign_list, create_campaign
from .views import ad_list, create_ad,track_click


urlpatterns = [
    path('', home, name='home'),
    path('campaigns/', campaign_list, name='campaign_list'),
    path('create/', create_campaign, name='create_campaign'),
    path('ads/', ad_list, name='ad_list'),
    path('ads/create/', create_ad, name='create_ad'),
    path('ads/click/<int:ad_id>/', track_click, name='track_click'),

]
