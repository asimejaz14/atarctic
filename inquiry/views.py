from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from inquiry.inquiry_controller import InquiryController


# Create your views here.
class InquiryView(APIView):
    inquiry_controller = InquiryController
    permission_classes = [AllowAny]

    def get(self, request, inquiry_id=None):
        return self.inquiry_controller.get_inquiry(request, inquiry_id)

    def post(self, request):
        return self.inquiry_controller.create_inquiry(request)

    def patch(self, request, inquiry_id):
        return self.inquiry_controller.update_inquiry(request, inquiry_id)
