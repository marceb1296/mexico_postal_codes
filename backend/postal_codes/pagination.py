from rest_framework.pagination import PageNumberPagination, _positive_int
from rest_framework.response import Response
import math


class CustomPagination(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "page_size"

    def get_page_size(self, request):
        if self.page_size_query_param in request.query_params:
            try:
                return _positive_int(
                    request.query_params[self.page_size_query_param],
                    strict=True,
                    cutoff=self.max_page_size
                )
            except (KeyError, ValueError):
                pass

        return self.page_size

    def get_paginated_response(self, data):

        # you can count total page from request by total and page_size
        total_page = math.ceil(
            self.page.paginator.count / self.get_page_size(self.request))

        # here is your response
        return Response({
            'count': self.page.paginator.count,
            'total_pages': total_page or 1,
            'current_page': self.page.number,
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
            'results': data
        })
