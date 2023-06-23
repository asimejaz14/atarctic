from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT

from design.models import Design


class BannerController:

    @classmethod
    def get_banner_image(cls, request):
        banner_image = Design.objects.first()
        if banner_image:
            return Response(data=banner_image.banner.url, status=HTTP_200_OK)
        return Response(data=None, status=HTTP_204_NO_CONTENT)

    @classmethod
    def post_banner_image(cls, request):
        design = Design.objects.first()
        if design:
            design.banner.delete()
            design.banner = request.data.get('banner')
            design.save()
            return Response(data=design.banner.url, status=HTTP_200_OK)
        design = Design.objects.create(banner=request.data.get('banner'))

        return Response(data=design.banner.url, status=HTTP_200_OK)


class FooterController:

    @classmethod
    def get_footer_text(cls, request):
        footer = Design.objects.first()
        if footer:
            return Response(data=footer.footer, status=HTTP_200_OK)
        return Response(data=None, status=HTTP_204_NO_CONTENT)

    @classmethod
    def post_footer_text(cls, request):
        footer = Design.objects.first()
        if footer:
            footer.footer = request.data.get('footer')
            footer.save()
            return Response(data=footer.footer, status=HTTP_200_OK)
        footer = Design.objects.create(footer=request.data.get('footer'))

        return Response(data=footer, status=HTTP_200_OK)


class AboutController:

    @classmethod
    def get_about_text(cls, request):
        about = Design.objects.first()
        if about:
            return Response(data=about.about, status=HTTP_200_OK)
        return Response(data=None, status=HTTP_204_NO_CONTENT)

    @classmethod
    def post_about_text(cls, request):
        about = Design.objects.first()
        if about:
            about.about = request.data.get('about')
            about.save()
            return Response(data=about.about, status=HTTP_200_OK)
        about = Design.objects.create(about=request.data.get('about'))

        return Response(data=about, status=HTTP_200_OK)
