from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT, HTTP_500_INTERNAL_SERVER_ERROR
)

from common.enums import Status, FAQ_SORTING_KEYS
from common.utils import get_default_query_param
from .models import FAQ
from .serializers import FAQSerializer


class FAQController:
    @classmethod
    def get_faq(cls, request, faq_id=None):
        try:
            # Single FAQ detail
            if faq_id:
                faq = FAQ.objects.filter(id=faq_id).first()
                if not faq:
                    return Response(data=None, status=HTTP_204_NO_CONTENT)
                serialized_faq = FAQSerializer(faq)
                return Response(data=serialized_faq.data, status=HTTP_200_OK)
            kwargs = {}
            order_by = get_default_query_param(request, "order_by", "created_at")
            order = get_default_query_param(request, "order", "desc")

            if order == "asc":
                sort = FAQ_SORTING_KEYS[order_by]
            else:
                sort = "-" + FAQ_SORTING_KEYS[order_by]

            kwargs['status'] = Status.ACTIVE
            # All FAQs
            faqs = FAQ.objects.filter(**kwargs).order_by(sort)
            count = faqs.count()
            if not faqs:
                return Response(data=None, status=HTTP_204_NO_CONTENT)
            serialized_faqs = FAQSerializer(faqs, many=True)
            return Response(data={"count": count, "data": serialized_faqs.data}, status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data=str(e), status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def create_faq(cls, request):
        try:
            serialized_faq = FAQSerializer(data=request.data)
            if serialized_faq.is_valid():
                serialized_faq.save()
                return Response(data=serialized_faq.data, status=HTTP_201_CREATED)
            return Response(data=serialized_faq.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(data=str(e), status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def update_faq(cls, request, faq_id=None):
        try:
            faq = FAQ.objects.get(id=faq_id)
            serialized_faq = FAQSerializer(faq, data=request.data, partial=True)
            if serialized_faq.is_valid():
                serialized_faq.save()
                return Response(data=serialized_faq.data, status=HTTP_200_OK)
            return Response(data=serialized_faq.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(data=str(e), status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def delete_faq(cls, request, faq_id):
        try:
            faq = FAQ.objects.get(id=faq_id)
            faq.delete()
            return Response(data=None, status=HTTP_204_NO_CONTENT)
        except FAQ.DoesNotExist:
            return Response(data=None, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(data=str(e), status=HTTP_500_INTERNAL_SERVER_ERROR)
