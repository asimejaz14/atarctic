from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED, \
    HTTP_400_BAD_REQUEST

from common.enums import INQUIRY_SORTING_KEYS
from common.utils import get_default_query_param
from inquiry.models import Inquiry
from inquiry.serializers import InquirySerializer


class InquiryController:
    @classmethod
    def get_inquiry(cls, request, inquiry_id=None):
        try:
            # single order detail
            if inquiry_id:
                inquiry = Inquiry.objects.filter(id=inquiry_id).first()
                if not inquiry:
                    return Response(data=None, status=HTTP_204_NO_CONTENT)
                serialized_order = InquirySerializer(inquiry)
                return Response(data=serialized_order.data, status=HTTP_200_OK)

            # all products
            kwargs = {}
            order_by = get_default_query_param(request, "order_by", "created_at")
            order = get_default_query_param(request, "order", "asc")
            limit = get_default_query_param(request, "limit", None)
            offset = get_default_query_param(request, "offset", None)

            if order == "asc":
                sort = INQUIRY_SORTING_KEYS[order_by]
            else:
                sort = "-" + INQUIRY_SORTING_KEYS[order_by]

            inquiry = Inquiry.objects.filter(**kwargs).order_by(sort)

            count = inquiry.count()
            if limit and offset:
                pagination = LimitOffsetPagination()
                inquiry = pagination.paginate_queryset(inquiry, request)
            if not inquiry:
                return Response(data=None, status=HTTP_204_NO_CONTENT)
            serialized_inquiry = InquirySerializer(inquiry, many=True)
            return Response(data={"count": count, "data": serialized_inquiry.data}, status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def create_inquiry(cls, request):
        try:
            serialized_inquiry = InquirySerializer(data=request.data)
            if serialized_inquiry.is_valid():
                serialized_inquiry.save()
                return Response(data=serialized_inquiry.data, status=HTTP_201_CREATED)
            return Response(data=serialized_inquiry.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def update_inquiry(cls, request, inquiry_id=None):
        try:
            inquiry = Inquiry.objects.get(id=inquiry_id)
            serialized_inquiry = InquirySerializer(inquiry, data=request.data, partial=True)
            if serialized_inquiry.is_valid():
                serialized_inquiry.save()
                return Response(data=serialized_inquiry.data, status=HTTP_200_OK)
            return Response(data=serialized_inquiry.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)
