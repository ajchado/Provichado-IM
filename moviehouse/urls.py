from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

#paths arranged alphabetically by name
app_name = 'moviehouse'

urlpatterns = [
    #path('api/data', views.get_data, name='api-data')
    
    path('index', views.MovieHouseIndexView.as_view(), name="index_view"),
    path('main', views.MovieHouseLandingView.as_view(), name="landing_view"),
    path('dvdregistration', views.MovieHouseDvdRegistrationView.as_view(), name="dvdregistration_view"),
#   path('customerregistration', views.MovieHouseCustomerRegistrationView.as_view(), name="customerregistration_view"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
