from django.db import models
from django.utils.translation import gettext_lazy as _
from io import BytesIO
from PIL import Image

from django.core.files.uploadedfile import InMemoryUploadedFile
from .utils import (get_unique_slug, get_unique_sku, 
                    get_unique_string)
from users.models import (User)
from products.utils import (upload_photo)


""" upload to function definition """
def upload_to(instance, filename):
    return '{filename}'.format(filename=filename)


""" different brand endorsed with the system """
class brand(models.Model):
    brandName = models.CharField(default="GD-Shop", null=False, 
                                 blank=False, max_length=60)
    brandIcon = models.ImageField(upload_to='', default="logo.jpg", 
                                    null=False)

    def save(self, *args, **kwargs):
        if self.brandIcon:
            self.brandIcon = upload_photo(80, 'brandIcon', 'JPEG',
                                          self.brandIcon)    
        super().save(*args, **kwargs)

    def __str__(self):
        return self.brandName


"""category table containing main category of products,
    shoes for mens can be one category"""
class categories(models.Model):
    categoryName = models.CharField(default="Men", null=False, max_length=60)
    categoryIcon = models.ImageField(_("Image"), upload_to=upload_to, 
                                    default="logo.jpg", null=False)

    def save(self, *args, **kwargs):
        if self.categoryIcon:
            self.categoryIcon = upload_photo(80, 'categoryIcon', 'JPEG',
                                             self.categoryIcon)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.categoryName
 

"""subcategory table containing subcategory of products,
    formal men shoes is subcategory for men category"""
class subcategories(models.Model):
    subcategoryName = models.CharField(default="Formal", null=False,
                                       max_length=60)
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE,
                                    related_name="subcategories")

    def __str__(self):
        return self.subcategoryName+" "+self.category_id.categoryName

    class Meta:
        unique_together = ('subcategoryName', 'category_id')


""" main product table with generic informations of the products"""
class products(models.Model):
    productName = models.CharField(default="Shoes", null="False",
                                   max_length=250)
    slug = models.SlugField(null=True, blank=True)
    categoryName = models.CharField(default="Men", null="False",
                                    max_length=60)
    subcategoryName = models.CharField(default="Formal", null=False,
                                       max_length=60)
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(subcategories,
                                       on_delete=models.CASCADE)
    description_long = models.TextField(null=True, blank=True)
    description_short = models.TextField(null=True, blank=True)
    previewImg = models.ImageField(_("Image"), upload_to=upload_to,
                                   default="logo.jpg", null=False)
    is_featured = models.BooleanField(default=False, null=False)
    price = models.FloatField(default=1000.00, blank=False, null=False)
    stock = models.IntegerField(default=50, blank=False, null=False)
    brand_id = models.ForeignKey(brand, on_delete=models.CASCADE,
                                 null=True, blank=True)
    description1 = models.TextField(null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)
    features1 = models.CharField(null=True, blank=True, max_length=250)
    features2 = models.CharField(null=True, blank=True, max_length=250)
    features3 = models.CharField(null=True, blank=True, max_length=250)
    features4 = models.CharField(null=True, blank=True, max_length=250)
    features5 = models.CharField(null=True, blank=True, max_length=250)
    features6 = models.CharField(null=True, blank=True, max_length=250)
    features7 = models.CharField(null=True, blank=True, max_length=250)
    discounted_price = models.FloatField(null=True, blank=True)
    delivery_time = models.CharField(null=True, blank=True, max_length=150)
    warranty = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.productName

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'productName', 'slug')
        self.categoryName = self.category_id.categoryName
        self.subcategoryName = self.subcategory_id.subcategoryName
        super().save(*args, **kwargs)


""" store generic types of variations, variations maybe size, color etc."""
class variations(models.Model):
    variationName=models.CharField(default="Size", null="False",
                                   max_length=250)

    def __str__(self):
        return self.variationName


""" store generic variations options, variations options maybe big, large,
    red, blue etc"""
class variations_options(models.Model):
    variationValue = models.CharField(default="Large", null="False",
                                      max_length=250)
    variation_id = models.ForeignKey(variations, on_delete=models.CASCADE)

    def __str__(self):
        return self.variationValue


""" map product with its available variations from variations table """
class product_variations(models.Model):
    variationName = models.CharField(default="Size", null="False",
                                     max_length=250)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)

    def __str__(self):
        if self.variationName is None:
            return " "
        else:
            return self.variationName


""" map product with its available variations options,
    from variations options table"""
class product_variations_options(models.Model):
    variationValue = models.CharField(default="Large", null="False",
                                      max_length=250)
    product_variation_id = models.ForeignKey(product_variations,
                                             on_delete=models.CASCADE)

    # def __str__(self):
    #     return (self.variationValue+" "+
    #             self.product_variation_id.variationName
    #             +" "+self.product_variation_id.product_id.productName)


""" details about every combinations that each product can have,
    like black-small-jeans can be one combination """
class products_combinations(models.Model):
    combination_string = models.CharField(default="Large-red", null="False",
                                          max_length=250)
    sku = models.CharField(default="lr", null="False", max_length=250)
    price = models.FloatField(default=2000.00, null=False)
    discounted_price = models.FloatField(null=True, blank=True)
    unique_string_id = models.CharField(default="aeeglrr", null=False,
                                        max_length=250)
    availableStock = models.IntegerField(default=50, null=False)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.combination_string)

    def save(self,*args, **kwargs):
        self.sku = get_unique_sku(self, self.combination_string, self.sku)
        self.unique_string_id = get_unique_string(self, self.combination_string,
                                                  self.unique_string_id)
        super().save(*args, **kwargs)
    

""" product stock information for each and every product combination """
class products_stocks(models.Model):
    totalstock = models.IntegerField(default=0, null=False, blank=False)
    unitPrice = models.FloatField(default=0.0, null=False, blank=False)
    products_combinations_id = models.ForeignKey(products_combinations,
                                                 on_delete=models.CASCADE)

    def __str__(self):
        return str(self.products_combinations_id)+" "+str(self.totalstock)

    def save(self, *args, **kwargs):
        a = products_combinations.objects.get(
                    pk=self.products_combinations_id.id)
        a.availableStock = self.totalstock
        a.price = self.unitPrice
        a.save()


""" image galleries for the storage of product images"""
class image_galleries(models.Model):
    product_combination = models.CharField(blank=True, null=True,
                                           max_length=100)
    small = models.ImageField(_("Image"), upload_to=upload_to,
                              default="logo.jpg", null=False)
    image1 = models.ImageField(_("Image"), upload_to=upload_to,
                               default="logo.jpg", null=False)
    image2 = models.ImageField(_("Image"), upload_to=upload_to,
                                 default="logo.jpg", null=False)
    image3 = models.ImageField(_("Image"), upload_to=upload_to,
                                 default="logo.jpg", null=False)

    def save(self, *args, **kwargs):
        if self.small:
            self.small = upload_photo(80, 'smallProduct', 'JPEG', self.small)
        if self.image1:
            self.image1 = upload_photo(80, 'image1Product', 'JPEG',
                                       self.image1)
        if self.image2:
            self.image2 = upload_photo(80, 'image2Product', 'JPEG',
                                       self.image2)
        if self.image3:
            self.image3 = upload_photo(80, 'image3Product', 'JPEG',
                                       self.image3)
        super().save(self, *args, **kwargs)
    
    def __str__(self):
        return "Image_Gallery"+ str(self.id)


""" mapping image galleries with the individual product informations"""
class product_images(models.Model):
    is_featured = models.BooleanField(default=False, null=False)
    image_galleries_id = models.ForeignKey(image_galleries,
                                           on_delete=models.CASCADE)
    product_variations_value_id = models.ForeignKey(products_combinations,
                                           on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_variations_value_id)


""" cache database incase redis is not implemented """
class product_cache(models.Model):
    slug = models.SlugField(null=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    data = models.TextField()

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'product_id.productName',
                                        'slug')
        super(self).save()


""" list of all the suscribers email """
class suscribers(models.Model):
    email = models.CharField(default="info@gdshopnepal.com", max_length=100,
                             null=False, blank=False)

    def __str__(self):
        return self.email


""" list of the common categories"""
class CommonCategories(models.Model):
    category = models.ForeignKey(categories,
                                 on_delete=models.CASCADE)
    category_picture = models.ImageField(_("Image"), upload_to=upload_to, 
                                         default="logo.jpg", null=False)

    def save(self, *args, **kwargs):
        if self.category_picture:
            self.category_picture = upload_photo(80, 'categoryPicture',
                                                 'JPEG',
                                                 self.category_picture)
        super(self).save()


""" different festive seasons """
class FestiveSeasons(models.Model):
    festive_season_name = models.CharField(max_length=250, null=True,
                                           blank=True)
    festive_season_picture = models.ImageField(_("Image"),
                                               upload_to=upload_to, 
                                               default="logo.jpg",
                                               null=False)
    festive_season_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.festive_season_picture:
            self.festive_season_picture = upload_photo(80, 'festiveSeason',
                                            'JPEG',
                                            self.festive_season_picture)
        super(FestiveSeasons, self).save()
    

""" festive season to product map """
class FestiveSeasonProducts(models.Model):
    festive_season = models.ForeignKey(FestiveSeasons,
                                       on_delete=models.CASCADE,
                                       related_name="festive_season")
    products = models.ForeignKey(products,
                                 on_delete=models.CASCADE)
    


""" client session """
class ClientSession(models.Model):
    uid = models.UUIDField(primary_key=True)
    client_ip = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    is_logged = models.BooleanField(default=False, null=False, blank=False)
    session_count = models.IntegerField(default=0, blank=False, null=False)
    logged_user = models.ForeignKey(User, on_delete=models.CASCADE,
                                    null=True, blank=True)


""" client session and cart mapping """
class ClientSessionCartMap(models.Model):
    client_session = models.ForeignKey(ClientSession,
                                       on_delete=models.CASCADE)
    products = models.ForeignKey(products_combinations,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=False, blank=False)


""" client session and wishlist mapping """
class ClientSessionWishListMap(models.Model):
    client_session = models.ForeignKey(ClientSession,
                                       on_delete=models.CASCADE)
    product_combinations = models.ForeignKey(products_combinations,
                                             on_delete=models.CASCADE)
    products = models.ForeignKey(products, on_delete=models.CASCADE)


""" review for every products """
class ReviewProducts(models.Model):
    ratings = models.IntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    reply = models.TextField(null=True, blank=True)
    products = models.ForeignKey(products, on_delete=models.CASCADE, 
                                 null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)