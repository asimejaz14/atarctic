from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, \
    HTTP_204_NO_CONTENT

from common.enums import PARTNER_SORTING_KEYS
from common.utils import get_default_query_param
from partner.models import Partner, PartnerMedia
from partner.serializers import PartnerSerializer


class PartnerController:

    @classmethod
    def get_partner(cls, request, partner_id=None):
        try:
            # single order detail
            if partner_id:
                partner = Partner.objects.filter(id=partner_id).first()
                if not partner:
                    return Response(data=None, status=HTTP_204_NO_CONTENT)
                serialized_partner = PartnerSerializer(partner)
                return Response(data=serialized_partner.data, status=HTTP_200_OK)

            # all products
            kwargs = {}
            order_by = get_default_query_param(request, "order_by", "index")
            order = get_default_query_param(request, "order", "asc")
            # category = get_default_query_param(request, "category", "all")
            display = get_default_query_param(request, "display", None)
            # limit = get_default_query_param(request, "limit", None)
            # offset = get_default_query_param(request, "offset", None)

            # if category == "fruit":
            #     kwargs['category__icontains'] = 'fruit'
            # elif category == "vegetable":
            #     kwargs['category__icontains'] = 'vegetable'

            # if display == "homepage":
            #     kwargs['status'] = Status.ACTIVE

            if order == "asc":
                sort = PARTNER_SORTING_KEYS[order_by]
            else:
                sort = "-" + PARTNER_SORTING_KEYS[order_by]

            partner = Partner.objects.filter(**kwargs).order_by(sort)

            count = partner.count()
            # if limit and offset:
            #     pagination = LimitOffsetPagination()
            #     products = pagination.paginate_queryset(products, request)
            if not partner:
                return Response(data=None, status=HTTP_204_NO_CONTENT)
            serialized_partner = PartnerSerializer(partner, many=True)
            return Response(data={"count": count, "data": serialized_partner.data}, status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def create_partner(cls, request):
        try:
            serialized_partner = PartnerSerializer(data=request.data)
            if serialized_partner.is_valid():
                serialized_partner.save()
                return Response(data=serialized_partner.data, status=HTTP_201_CREATED)
            return Response(data=serialized_partner.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def update_partner(cls, request, partner_id=None):
        try:
            partner = Partner.objects.get(id=partner_id)
            serialized_partner = PartnerSerializer(partner, data=request.data, partial=True)
            if serialized_partner.is_valid():
                serialized_partner.save()
                return Response(data=serialized_partner.data, status=HTTP_200_OK)
            return Response(data=serialized_partner.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def delete_partner(cls, request, partner_id=None):
        try:
            Partner.objects.filter(id=partner_id).delete()
            return Response(data=None, status=HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

class ImageController:

    @classmethod
    def delete_image(cls, request, image_id=None):
        try:
            PartnerMedia.objects.filter(id=image_id).delete()
            return Response(data=None, status=HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)