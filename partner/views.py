from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from partner.partner_controller import PartnerController


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
