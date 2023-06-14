import os

from rest_framework import serializers

from AtArctic import settings
from product.models import Product, ProductMedia


class GetProductSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField()

    def get_media(self, obj):
        docs = []
        try:
            files = ProductMedia.objects.filter(product=obj)
            for file in files:
                # docs.append(file.media.url)
                # docs.append(file.media.url)
                docs.append({
                    "id": file.id,
                    "file": file.media.url
                })
            return docs
        except:
            return docs
    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField()

    def get_media(self, obj):
        try:
            files = []
            if self.context["request"].method == "POST":
                if self.context.get("media"):
                    for file in self.context["media"]:
                        media_file = ProductMedia.objects.create(
                            product=obj, media=file
                        )
                        # files.append(media_file.media.url)
                        files.append({
                            "id": media_file.id,
                            "file": media_file.media.url
                        })
                    return files
                else:
                    return None
            elif self.context["request"].method == "PATCH":

                # for media_ in product_media_files:
                #     os.remove(media_.media.path)
                if self.context.get("media"):
                    for file in self.context["media"]:
                        ProductMedia.objects.create(
                            product=obj, media=file
                        )
                        # files.append(media_file.media.url)
                        # files.append(media_file.media.url)
                    product_media_files = ProductMedia.objects.filter(product_id=obj.id)
                    for media_file in product_media_files:
                        files.append({
                            "id": media_file.id,
                            "file": media_file.media.url
                        })
                    return files

                else:
                    docs = []
                    files = ProductMedia.objects.filter(product=obj)
                    for file in files:
                        # docs.append(file.media.url)
                        # docs.append(file.media.url)
                        docs.append({
                            "id": file.id,
                            "file": file.media.url
                        })
                    return docs if docs else None
            return None
        except Exception as e:
            print("ERROR HERE", e)
            return None

    class Meta:
        model = Product
        fields = "__all__"
