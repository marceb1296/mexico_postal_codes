from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import PostalCode
from .serializer import PostalCodeSerializer

from .pagination import CustomPagination

# Create your views here.


class GetPostalCodePagination(ListAPIView):

    pagination_class = CustomPagination
    serializer_class = PostalCodeSerializer
    pagination_number = 10
    max_page_size = 50

    @property
    def get_query_params(self):

        query_params_search = self.request.query_params

        return {
            "%s__icontains" % key: value for key, value in query_params_search.items() if key in [pc.name for pc in PostalCode._meta.fields]
        }

    def get_queryset(self):

        kwargs = self.get_query_params

        if kwargs:
            return PostalCode.objects.filter(**kwargs)

        return PostalCode.objects.filter()

    def list(self, *args, **kwargs):
        self.pagination_class.page_size = self.pagination_number
        self.pagination_class.max_page_size = self.max_page_size

        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)


class GetPostalCodeList(GetPostalCodePagination):

    def get_queryset(self):

        kwargs = self.get_query_params

        if kwargs:

            return PostalCode.objects.filter(**kwargs) if self.request.query_params.get("no_limit") == "true" else PostalCode.objects.filter(**kwargs)[0:self.max_page_size]

        return PostalCode.objects.all() if self.request.query_params.get("no_limit") == "true" else PostalCode.objects.all()[0:self.max_page_size]

    def list(self, *args, **kwargs):

        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
