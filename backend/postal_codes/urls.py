
from django.urls import path
from django.views.decorators.cache import cache_page
from .views import GetPostalCodeList, GetPostalCodePagination

urlpatterns = [
    path('v1/postal_codes', cache_page(60 * 60 * 4)
         (GetPostalCodePagination.as_view())),
    path('v2/postal_codes', cache_page(60 * 60 * 4)
         (GetPostalCodeList.as_view())),
]
