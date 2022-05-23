from django.contrib import admin

from .models import (categories, subcategories, products, product_variations,
                     product_variations_options, products_combinations,
                     image_galleries, product_images, product_cache,
                     products_stocks, brand, ClientSession,
                     ClientSessionCartMap, ClientSessionWishListMap, 
                     CommonCategories, ReviewProducts, variations,
                     variations_options, FestiveSeasons,
                     FestiveSeasonProducts)


# Register your models here.
admin.site.register(categories)
admin.site.register(subcategories)
admin.site.register(products)
admin.site.register(product_variations)
admin.site.register(product_variations_options)
admin.site.register(products_combinations)
admin.site.register(image_galleries)
admin.site.register(product_images)
admin.site.register(variations_options)
admin.site.register(variations)
admin.site.register(product_cache)
admin.site.register(products_stocks)
admin.site.register(brand)
admin.site.register(ClientSession)
admin.site.register(ClientSessionCartMap)
admin.site.register(ClientSessionWishListMap)
admin.site.register(CommonCategories)
admin.site.register(ReviewProducts)
admin.site.register(FestiveSeasons)
admin.site.register(FestiveSeasonProducts)