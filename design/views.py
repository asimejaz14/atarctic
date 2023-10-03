from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from design.design_controller import BannerController, MissionController
from design.design_controller import FooterController

from design.design_controller import AboutController


class BannerView(APIView):
    banner_controller = BannerController
    permission_classes = [AllowAny]

    def get(self, request):
        return self.banner_controller.get_banner_image(request)

    def post(self, request):
        return self.banner_controller.post_banner_image(request)


class FooterView(APIView):
    footer_controller = FooterController
    permission_classes = [AllowAny]

    def get(self, request):
        return self.footer_controller.get_footer_text(request)

    def post(self, request):
        return self.footer_controller.post_footer_text(request)


class AboutView(APIView):
    about_controller = AboutController
    permission_classes = [AllowAny]

    def get(self, request):
        return self.about_controller.get_about_text(request)

    def post(self, request):
        return self.about_controller.post_about_text(request)


class MissionView(APIView):
    mission_controller = MissionController
    permission_classes = [AllowAny]

    def get(self, request):
        return self.mission_controller.get_mission_text(request)

    def post(self, request):
        return self.mission_controller.post_mission_text(request)

    def patch(self, request):
        return self.mission_controller.update_mission_text(request)

    def delete(self, request):
        return self.mission_controller.delete_mission_text(request)
