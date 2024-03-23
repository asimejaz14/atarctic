from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from partner.partner_controller import PartnerController, ImageController


# Create your views here.
class PartnerView(APIView):
    partner_controller = PartnerController
    permission_classes = [AllowAny]

    def get(self, request, partner_id=None):
        return self.partner_controller.get_partner(request, partner_id)

    def post(self, request):
        return self.partner_controller.create_partner(request)

    def patch(self, request, partner_id=None):
        return self.partner_controller.update_partner(request, partner_id)

    def delete(self, request, partner_id=None):
        return self.partner_controller.delete_partner(request, partner_id)


class FileView(APIView):
    image_controller = ImageController
    permission_classes = [AllowAny]

    def delete(self, request, image_id=None):
        return self.image_controller.delete_image(request, image_id)