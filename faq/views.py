from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .faq_controller import FAQController


class FAQView(APIView):
    faq_controller = FAQController
    permission_classes = [AllowAny]

    def get(self, request, faq_id=None):
        return self.faq_controller.get_faq(request, faq_id)

    def post(self, request):
        return self.faq_controller.create_faq(request)

    def patch(self, request, faq_id):
        return self.faq_controller.update_faq(request, faq_id)

    def delete(self, request, faq_id):
        return self.faq_controller.delete_faq(request, faq_id)
