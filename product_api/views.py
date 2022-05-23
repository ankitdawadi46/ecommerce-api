import datetime

from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (IsAuthenticated, AllowAny,
                                        IsAdminUser)
from django_filters.rest_framework import DjangoFilterBackend

from products.models import (ClientSession, ClientSessionCartMap,
                             ClientSessionWishListMap, CommonCategories,
                             FestiveSeasonProducts, FestiveSeasons,
                             ReviewProducts, brand, products,
                             products_combinations,
                             product_images, categories, subcategories,
                             product_variations, product_variations_options,
                             variations_options, variations, products_stocks,
                             image_galleries)
from product_api.serializers import (ClientSessionCartMapSerializers,
                                     ClientSessionSerializers,
                                     ClientSessionWishListMapSerializers,
                                     CommonCategoriesSerializers, FestiveSeasonListSerializer,
                                     FestiveSeasonsProductsSerializers,
                                     FestiveSeasonsSerializers,
                                     ProductsSerializer,
                                     ProductImagesSerializers,
                                     ProductCombinationSerializer,
                                     CategoriesSerializer, ReviewProductsSerializers,
                                     SubcategoriesSerializer,
                                     ProductVariationsSerializers,
                                     ProductsVariationsOptionsSerializers,
                                     ProductImagesSerializers,
                                     VariationsSerializers,
                                     VariationsOptionsSerializers,
                                     ProductStocksSerializers,
                                     ImageGalleriesSerializers,
                                     BrandSerializer,)


""" permission for different crud operations """
class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """
    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False


class BrandList(viewsets.ModelViewSet):
    queryset = brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id','brandName']
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }


class ProductList(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'categoryName', 'subcategoryName',
                     'productName', 'brand_id']
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }

    def get_object(self, queryset = None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(products,slug=item)

    def get_queryset(self):
        return products.objects.select_related('brand_id',
                                               'category_id',
                                               'subcategory_id',
                                               'subcategory_id__category_id')

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        # For debugging purposes only.
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        queries = ['{}\n'.format(query['sql']) for query in connection.queries]
        print('queries: \n{}'.format(''.join(queries)))
        return response


""" views for the latest product display """
class NewProductList(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['categoryName', 'subcategoryName']
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }

    def get_object(self, queryset = None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(products,slug=item)

    def get_queryset(self):
        product = (products.objects.select_related('brand_id',
                                               'category_id',
                                               'subcategory_id',
                                               'subcategory_id__category_id')
                                               .order_by('-id')
                                               .exclude(is_featured = True))
        return product

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        # For debugging purposes only.
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        queries = ['{}\n'.format(query['sql']) for query in connection.queries]
        print('queries: \n{}'.format(''.join(queries)))
        return response


""" views for the featured product display """
class FeaturedProductList(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['categoryName', 'subcategoryName']
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }

    def get_object(self, queryset = None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(products, slug=item)

    def get_queryset(self):
        product = (products.objects.select_related('brand_id',
                                               'category_id',
                                               'subcategory_id',
                                               'subcategory_id__category_id')
                                               .filter(is_featured=True))
        return product

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        # For debugging purposes only.
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        queries = ['{}\n'.format(query['sql']) for query in connection.queries]
        print('queries: \n{}'.format(''.join(queries)))
        return response


class ProductVariations(viewsets.ModelViewSet):
    serializer_class = ProductVariationsSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['variationName', 'product_id']
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    } 

    def get_queryset(self):
        variations = product_variations.objects.select_related(
                        'product_id__category_id',
                        'product_id__subcategory_id__category_id',
                        'product_id__brand_id')
        return variations

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        # For debugging purposes only.
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        queries = ['{}\n'.format(query['sql']) for query in connection.queries]
        print('queries: \n{}'.format(''.join(queries)))
        return response


class ProductVariationsOptions(viewsets.ModelViewSet):
    serializer_class = ProductsVariationsOptionsSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['variationValue', 'product_variation_id']
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }

    def get_queryset(self):
        variations_options = product_variations_options.objects.select_related(
                                'product_variation_id__product_id__category_id',
                                'product_variation_id__product_id__subcategory_id__category_id',
                                'product_variation_id__product_id__brand_id')
        return variations_options

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        # For debugging purposes only.
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        queries = ['{}\n'.format(query['sql']) for query in connection.queries]
        print('queries: \n{}'.format(''.join(queries)))
        return response


class ProductCombinations(viewsets.ModelViewSet):
    serializer_class = ProductCombinationSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["combination_string", "sku", "unique_string_id",
                     "product_id"]
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    } 

    def get_queryset(self):
        productComb = (products_combinations
                          .objects
                          .select_related('product_id',
                                          'product_id__category_id',
                                          'product_id__subcategory_id',
                                          'product_id__brand_id',
                                          'product_id__subcategory_id__category_id'))
        return productComb

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        # For debugging purposes only.
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        queries = ['{}\n'.format(query['sql']) for query in connection.queries]
        print('queries: \n{}'.format(''.join(queries)))
        return response


class CategoriesName(viewsets.ModelViewSet):
    queryset = categories.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = CategoriesSerializer
    permission_classes = (ActionBasedPermission,)
    parser_classes = [MultiPartParser, FormParser]
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    } 


class SubCategoriesName(viewsets.ModelViewSet):
    queryset = subcategories.objects.select_related('category_id')
    serializer_class = SubcategoriesSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['subcategoryName','category_id']
    permission_classes = (ActionBasedPermission,)
    parser_classes = [MultiPartParser, FormParser]
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        # For debugging purposes only.
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        queries = ['{}\n'.format(query['sql']) for query in connection.queries]
        print('queries: \n{}'.format(''.join(queries)))
        return response


class VariationsName(viewsets.ModelViewSet):
    queryset = variations.objects.all()
    serializer_class = VariationsSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'variationName']
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }


class VariationsOptionsName(viewsets.ModelViewSet):
    queryset = variations_options.objects.select_related('variation_id')
    serializer_class = VariationsOptionsSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'variation_id', 'variationValue']
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }


class ProductStocks(viewsets.ModelViewSet):
    queryset = products_stocks.objects.all()
    serializer_class = ProductStocksSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['products_combinations_id', 'totalstock', 'unitPrice']
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }

    def get_object(self, queryset = None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(products_stocks,
                        products_combinations_id=item)


class ImageGalleries(viewsets.ModelViewSet):
    queryset = image_galleries.objects.all()
    serializer_class = ImageGalleriesSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'product_combination']
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }


class ProductImages(viewsets.ModelViewSet):
    queryset = product_images.objects.select_related('image_galleries_id',
                    'product_variations_value_id',
                    'product_variations_value_id__product_id__category_id',
                    'product_variations_value_id__product_id__subcategory_id',
                    'product_variations_value_id__product_id__brand_id',
                    'product_variations_value_id__product_id__subcategory_id__category_id')
    serializer_class = ProductImagesSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'product_variations_value_id',
                     'image_galleries_id']
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        # For debugging purposes only.
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        queries = ['{}\n'.format(query['sql']) for query in connection.queries]
        print('queries: \n{}'.format(''.join(queries)))
        return response


class CommonCategoriesViewSets(viewsets.ModelViewSet):
    queryset = CommonCategories.objects.select_related('category')
    serializer_class = CommonCategoriesSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'category']
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }


class FestiveSeasonsViewSets(viewsets.ModelViewSet):
    queryset = FestiveSeasons.objects.all()
    serializer_class = FestiveSeasonsSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'festive_season_name']
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',  'partial_update','update','destroy', 'create',],
      IsAdminUser: []
    }

    def dispatch(self, *args, **kwargs):
      response = super().dispatch(*args, **kwargs)
    # For debugging purposes only.
      from django.db import connection
      print('# of Queries: {}'.format(len(connection.queries)))
      queries = ['{}\n'.format(query['sql']) for query in connection.queries]
      print('queries: \n{}'.format(''.join(queries)))
      return response


class FestiveSeasonsProductViewSets(viewsets.ModelViewSet):
    queryset = FestiveSeasonProducts.objects.select_related(
                  'festive_season',
                  'products__category_id',
                  'products__subcategory_id__category_id',
                  'products__brand_id',)
    serializer_class = FestiveSeasonsProductsSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'festive_season', 'products']
    permisssion_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }


class ClientSessionViewSets(viewsets.ModelViewSet):
    queryset = ClientSession.objects.select_related('logged_user')
    serializer_class = ClientSessionSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['uid', 'client_ip', 'is_logged', 'logged_user']
    permisssion_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }


class ClientSessionCartMapViewSets(viewsets.ModelViewSet):
    queryset = ClientSessionCartMap.objects.all()
    serializer_class = ClientSessionCartMapSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'client_session', 'products']
    permisssion_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }


class ClientSessionWishListMapViewSets(viewsets.ModelViewSet):
    queryset = ClientSessionWishListMap.objects.all()
    serializer_class = ClientSessionWishListMapSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'client_session', 'products', 
                     'product_combinations']
    permisssion_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        # For debugging purposes only.
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        queries = ['{}\n'.format(query['sql']) for query in connection.queries]
        print('queries: \n{}'.format(''.join(queries)))
        return response


class ReviewProductsViewSets(viewsets.ModelViewSet):
    queryset = ReviewProducts.objects.all()
    serializer_class = ReviewProductsSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'user', 'products', 'ratings']
    permisssion_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
      IsAdminUser: ['update', 'partial_update', 'destroy', 'create',]
    }

  
""" this is viewset for normalized form of data form the festive season
    and products"""
class FestiveSeasonListViewSets(viewsets.ModelViewSet):
    queryset = FestiveSeasons.objects.all()
    serializer_class = FestiveSeasonListSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'festive_season_name', 'is_active']
    permisssion_classes = (ActionBasedPermission,)
    action_permissions = {
      AllowAny: ['retrieve', 'list',],
    }