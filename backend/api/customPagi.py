from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


'''Any Pagination You Use It Must Be Ordered Otherwise You Will Get Warning...!'''

class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'records' # Custom Changeable Pagination From Server.
    max_page_size = 5 # Maximum Pagination Size.

    # page_query_param = 'mypage' # instead of 'page'.
    # last_page_strings = 'end' # default is last : ?page=last
    # now : ?page=end

class CustomLimitOffsetPagination(LimitOffsetPagination):
    # default_limit = 3
    # max_limit = 5

    limit_query_param = 'max' # default is 'limit'
    offset_query_param = 'start' # default is 'offset'

class CustomCursorPagination(CursorPagination):
    '''
    created : This must be added in models. (Timestamp).
    <<Previous  >>Next  : only.

    if created is not present then error :- "Cannot resolve keyword 'created' into field. Choices are: city, id, name, roll"
    '''

    page_size = 3
    ordering = '-name' # Default is 'created' : # if created is not specified then you have to specify.
    cursor_query_param = 'myCursor' # Default is 'cursor'
