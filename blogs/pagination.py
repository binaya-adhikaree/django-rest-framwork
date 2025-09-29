from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size=6
    page_size_query_param ='page_size'
    page_query_param="blog_id"
    max_page_size=1


    def get_paninated_response(self, data):
        return Response({
            "next":self.get_next_link(),
            "previous":self.get_previous_link(),
            "count":self.page.paginator.count,
            "prev_size":self.page_size,
            "results":data
        })
    
    