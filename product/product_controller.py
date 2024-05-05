from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_201_CREATED, \
    HTTP_400_BAD_REQUEST, HTTP_422_UNPROCESSABLE_ENTITY

from common.enums import PRODUCT_SORTING_KEYS, Status
from common.utils import get_default_query_param
from product.models import Product, ProductMedia
from product.serializers import ProductSerializer, GetProductSerializer


class ProductController:

    @classmethod
    def get_product(cls, request, product_id=None):
        try:
            # single order detail
            if product_id:
                order = Product.objects.filter(id=product_id).first()
                if not order:
                    return Response(data=None, status=HTTP_204_NO_CONTENT)
                serialized_order = GetProductSerializer(order)
                return Response(data=serialized_order.data, status=HTTP_200_OK)

            # all products
            kwargs = {}
            order_by = get_default_query_param(request, "order_by", "index")
            order = get_default_query_param(request, "order", "asc")
            category = get_default_query_param(request, "category", "all")
            display = get_default_query_param(request, "display", None)
            # limit = get_default_query_param(request, "limit", None)
            # offset = get_default_query_param(request, "offset", None)

            if category == "fruit":
                kwargs['category__icontains'] = 'fruit'
            elif category == "vegetable":
                kwargs['category__icontains'] = 'vegetable'

            if display == "homepage":
                kwargs['status'] = Status.ACTIVE
                kwargs['is_display'] = True # to show on homepage

            if display == "services":
                kwargs['status'] = Status.ACTIVE

            if order == "asc":
                sort = PRODUCT_SORTING_KEYS[order_by]
            else:
                sort = "-" + PRODUCT_SORTING_KEYS[order_by]

            products = Product.objects.filter(**kwargs).order_by(sort)

            count = products.count()
            # if limit and offset:
            #     pagination = LimitOffsetPagination()
            #     products = pagination.paginate_queryset(products, request)
            if not products:
                return Response(data=None, status=HTTP_204_NO_CONTENT)
            serialized_orders = GetProductSerializer(products, many=True)
            return Response(data={"count": count, "data": serialized_orders.data}, status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def create_product(cls, request):
        try:
            media = request.FILES.getlist("media")
            serialized_product = ProductSerializer(data=request.data, context={"request": request, "media": media})
            if serialized_product.is_valid():
                serialized_product.save()
                return Response(data=serialized_product.data, status=HTTP_201_CREATED)
            return Response(data=serialized_product.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def update_product(cls, request, product_id=None):
        try:
            if not product_id:
                return Response(data=None, status=HTTP_422_UNPROCESSABLE_ENTITY)

            product = Product.objects.get(id=product_id)
            media = request.FILES.getlist("media")
            payload = request.data.copy()
            if not request.data.get("background_video"):
                payload.pop("background_video")
            serialized_product = ProductSerializer(product, data=request.data,
                                                   context={"request": request, "media": media}, partial=True)
            if serialized_product.is_valid():
                serialized_product.save()
                return Response(data=serialized_product.data, status=HTTP_200_OK)
            return Response(data=serialized_product.errors, status=HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def delete_product(cls, request, product_id=None):
        try:
            if not product_id:
                return Response(data=None, status=HTTP_422_UNPROCESSABLE_ENTITY)
            Product.objects.get(id=product_id).delete()
            return Response(data=None, status=HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)


class ImageController:

    @classmethod
    def delete_image(cls, request, image_id=None):
        try:
            ProductMedia.objects.filter(id=image_id).delete()
            return Response(data=None, status=HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)


class VideoController:

    @classmethod
    def delete_video(cls, request, product_id=None):
        try:
            product = Product.objects.get(id=product_id)
            product.background_video.delete()
            return Response(data=None, status=HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)


class IndexController:

    @classmethod
    def update_video(cls, request):
        try:
            product_id = request.data.get('id')
            new_index = request.data.get('index')
            product = Product.objects.get(id=product_id)
            old_index = product.index

            Product.objects.filter(index=new_index).update(index=old_index)
            product.index = new_index
            product.save()
            return Response(data=None, status=HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)
