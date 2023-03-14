from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    #path('', nyy, name='home'),
    path('', HomeRealEstate.as_view(), name='home'),
   # path('category/<int:category_id>', get_category, name='j'),
    path('test/', test, name='test'),
    path('registraton/', registration, name = 'registration'),
    path('login/', user_login, name = 'login'),
    path('logout/', user_logout, name = 'logout'),
    path('category/<int:category_id>', EstateCat.as_view(), name='j'),
    path('realestate/<int:pk>', ViewRealEstate.as_view(), name='h'),
    path('realestate/add_realestate', CreateEstate.as_view(), name='i'),
    ]
