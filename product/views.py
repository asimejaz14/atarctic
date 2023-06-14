from django.shortcuts import render
from rest_framework.permissions import AllowAny

# Create your views here.
from rest_framework.views import APIView

from product.product_controller import ProductController, ImageController, VideoController, IndexController


class ProductView(APIView):
    product_controller = ProductController
    permission_classes = [AllowAny]

    def get(self, request, product_id=None):
        return self.product_controller.get_product(request, product_id)

    def post(self, request):
        return self.product_controller.create_product(request)

    def patch(self, request, product_id=None):
        return self.product_controller.update_product(request, product_id)

    def delete(self, request, product_id=None):
        return self.product_controller.delete_product(request, product_id)


#
#
class FileView(APIView):
    image_controller = ImageController
    permission_classes = [AllowAny]

    def delete(self, request, image_id=None):
        return self.image_controller.delete_image(request, image_id)


class VideoView(APIView):
    video_controller = VideoController
    permission_classes = [AllowAny]

    def delete(self, request, product_id=None):
        return self.video_controller.delete_video(request, product_id)


class IndexView(APIView):
    index_controller = IndexController
    permission_classes = [AllowAny]

    def patch(self, request):
        return self.index_controller.update_video(request)
