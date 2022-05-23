from django.urls import path
from rest_framework.routers import DefaultRouter 
from django.conf.urls.static import static
from django.conf import settings

from .views import (FestiveSeasonListViewSets, ProductList, ProductStocks, ImageGalleries, ProductImages,
                    NewProductList, FeaturedProductList, ProductCombinations,
                    CategoriesName, SubCategoriesName, ProductVariations,
                    ProductVariationsOptions, VariationsName,
                    VariationsOptionsName, CommonCategoriesViewSets,
                    FestiveSeasonsViewSets, FestiveSeasonsProductViewSets,
                    ClientSessionViewSets, ClientSessionCartMapViewSets,
                    ClientSessionWishListMapViewSets, ReviewProductsViewSets)

app_name = 'product_api'

router = DefaultRouter()


router.register(r'allProduct', ProductList, basename="product")
router.register(r'newProduct', NewProductList, basename="newProduct")
router.register(r'featuredProduct', FeaturedProductList,
                basename="featureProduct")
router.register(r'productVariations', ProductVariations,
                basename="productVariations")
router.register(r'productVariationsOptions', ProductVariationsOptions,
                basename="productVariationsOptions")
router.register(r'productCombinations', ProductCombinations,
                basename="productCombinations")
router.register(r'categoriesName', CategoriesName, basename="categoriesName")
router.register(r'subcategoriesName', SubCategoriesName,
                basename="subcategoriesName")
router.register(r'variations', VariationsName, basename="variation")
router.register(r'variationsOptions', VariationsOptionsName,
                basename="variationsOptions")
router.register(r'productStocks', ProductStocks, basename="productstocks")
router.register(r'imageGalleries', ImageGalleries, basename="imagegalleries")
router.register(r'productImages', ProductImages, basename="productimages")
router.register(r'common-categories', CommonCategoriesViewSets,
                basename="common-categories")
router.register(r'festive-seasons', FestiveSeasonsViewSets,
                basename="festive-seasons")
router.register(r'festive-seasons-products', FestiveSeasonsProductViewSets,
                basename="festive-seasons-products")
router.register(r'client-session', ClientSessionViewSets,
                basename="client-session")
router.register(r'client-session-cart', ClientSessionCartMapViewSets,
                basename="client-session-cart")
router.register(r'client-session-wishlist', ClientSessionWishListMapViewSets,
                basename="client-session-wishlist")
router.register(r'review-products', ReviewProductsViewSets,
                basename="review-products")

""" these routers are for the list api only"""
router.register(r'show-festive-season-products', FestiveSeasonListViewSets,
                basename="show-festive-season-products")


urlpatterns= []
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)