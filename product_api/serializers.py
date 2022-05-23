from rest_framework import serializers
from products.models import (ClientSession, ClientSessionCartMap,
                             ClientSessionWishListMap, ReviewProducts,
                             products, products_combinations, categories,
                             subcategories, product_variations,
                             product_variations_options, products_stocks,
                             image_galleries, product_images,
                             product_cache, variations, variations_options,
                             brand, suscribers, CommonCategories,
                             FestiveSeasonProducts, FestiveSeasons)
from product_api.constants import BASE_URL
from products.utils import (DictSerializer)


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = brand
        fields = "__all__"


class CategoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = categories
        fields = "__all__"


class SubcategoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = subcategories
        fields = "__all__"

    def to_representation(self,instance):
        response = super().to_representation(instance)
        category = CategoriesSerializer(instance.category_id).data
        category['categoryIcon'] = (BASE_URL+str(category["categoryIcon"]))
        response['category_id'] = category
        return response


class ProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = products
        fields = "__all__"

    def to_representation(self,instance):
        response = super().to_representation(instance)
        category = CategoriesSerializer(instance.category_id).data
        category['categoryIcon'] = (BASE_URL+str(category["categoryIcon"]))
        response['category_id'] = category
        response['subcategory_id'] = SubcategoriesSerializer(
                                            instance.subcategory_id).data
        brand = BrandSerializer(instance.brand_id).data
        brand['brandIcon'] = BASE_URL+str(brand["brandIcon"])
        response['brand_id'] = brand
        return response


class ProductVariationsSerializers(serializers.ModelSerializer):

    class Meta:
        model = product_variations
        fields = "__all__"

    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['product_id'] = ProductsSerializer(
                                    instance.product_id).data
        return response


class ProductsVariationsOptionsSerializers(serializers.ModelSerializer):

    class Meta:
        model = product_variations_options
        fields = "__all__"

    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['product_variation_id'] = ProductVariationsSerializers(
                                                instance.product_variation_id).data
        return response


class VariationsSerializers(serializers.ModelSerializer):

    class Meta:
        model=variations
        fields="__all__"


class VariationsOptionsSerializers(serializers.ModelSerializer):
 
    class Meta:
        model= variations_options
        fields= "__all__"  

    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['variation_id'] = VariationsSerializers(
                                        instance.variation_id).data
        return response   


class ProductCombinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = products_combinations
        fields = "__all__"

    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['product_id'] = ProductsSerializer(instance.product_id).data
        return response


class ProductStocksSerializers(serializers.ModelSerializer):

    class Meta:
        model = products_stocks
        fields = "__all__"

    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['product_id'] = ProductCombinationSerializer(
                                    instance.products_combinations_id).data
        return response


class ImageGalleriesSerializers(serializers.ModelSerializer):

    class Meta:
        model = image_galleries
        fields = "__all__"


class ProductImagesSerializers(serializers.ModelSerializer):

    class Meta:
        model = product_images
        fields = "__all__"

    def to_representation(self,instance):
        response = super().to_representation(instance)
        picture = ImageGalleriesSerializers(instance.image_galleries_id).data
        picture_path1 = BASE_URL+str(picture["small"])
        picture["small"] = picture_path1
        picture_path2 = BASE_URL+str(picture["image1"])
        picture["image1"] = picture_path2
        picture_path3 = BASE_URL+str(picture["image2"])
        picture["image2"] = picture_path3
        picture_path4 = BASE_URL+str(picture["image3"])
        picture["image3"] = picture_path4
        response['image_galleries_id'] = picture
        response['product_variations_value_id'] = ProductCombinationSerializer(
                                                    instance
                                                    .product_variations_value_id).data
        return response


class ProductCacheSerializers(serializers.ModelSerializer):
    product_id = ProductsSerializer()

    class Meta:
        model = products
        fields = "__all__"


class CommonCategoriesSerializers(serializers.ModelSerializer):

    class Meta:
        model = CommonCategories
        fields = "__all__"


class FestiveSeasonsSerializers(serializers.ModelSerializer):

    class Meta:
        model = FestiveSeasons
        fields = "__all__"


class FestiveSeasonsProductsSerializers(serializers.ModelSerializer):

    class Meta:
        model = FestiveSeasonProducts
        fields = "__all__"


class ClientSessionSerializers(serializers.ModelSerializer):

    class Meta:
        model = ClientSession
        fields = "__all__"


class ClientSessionCartMapSerializers(serializers.ModelSerializer):

    class Meta:
        model = ClientSessionCartMap
        fields = "__all__"


class ClientSessionWishListMapSerializers(serializers.ModelSerializer):

    class Meta:
        model = ClientSessionWishListMap
        fields = "__all__"


class ReviewProductsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ReviewProducts
        fields = "__all__"


""" this is a single non nested serializer for sending normalized form of data,
    for products model"""
class ProductSingleSerializer(serializers.ModelSerializer):

    class Meta:
        model = products
        fields = "__all__"
        # list_serializer_class = DictSerializer


""" this is a single non nested serializer for sending normalized form of data,
    for festive season products model"""
class FestiveSeasonProductSerializer(serializers.ModelSerializer):
    products = ProductSingleSerializer()
    class Meta:
        model = FestiveSeasonProducts
        fields = "__all__"
        # list_serializer_class = DictSerializer


""" this is a single non nested serializer for sending normalized form of data,
    for festive season model"""
class FestiveSeasonListSerializer(serializers.ModelSerializer):
    festive_season = FestiveSeasonProductSerializer(many=True)

    class Meta:
        model = FestiveSeasons
        fields = "__all__"






