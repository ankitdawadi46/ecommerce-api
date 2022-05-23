from io import BytesIO
from PIL import Image
import threading

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.text import slugify
from rest_framework import serializers

 
class DictSerializer(serializers.ListSerializer):
    """
    Overrides default ListSerializer to return a dict with a custom field from
    each item as the key. Makes it easier to normalize the data so that there
    is minimal nesting. dict_key defaults to 'id' but can be overridden.
    """
    dict_key = 'id'
    @property
    def data(self):
        """
        Overriden to return a ReturnDict instead of a ReturnList.
        """
        ret = super(serializers.ListSerializer, self).data
        return ReturnDict(ret, serializer=self)
    def to_representation(self, data):
        """
        Converts the data from a list to a dictionary.
        """
        items = super(DictSerializer, self).to_representation(data)
        return {item[self.dict_key]: item for item in items}


def get_unique_slug(model_instance, slugable_field_name, slug_field_name):
    """
    Takes a model instance, sluggable field name (such as 'title') of that
    model as string, slug field name (such as 'slug') of the model as string;
    returns a unique slug as string.
    """
    slug = slugify(getattr(model_instance, slugable_field_name))
    unique_slug = slug
    extension = 1
    ModelClass = model_instance.__class__
 
    while ModelClass._default_manager.filter(
        **{slug_field_name: unique_slug}
    ).exists():
        unique_slug = '{}-{}'.format(slug, extension)
        extension += 1
 
    return unique_slug

def get_unique_sku(model_instance,combination_string_field,sku_field):
    sku = []
    for i in range(len(combination_string_field)):
        if i==0:
            print(combination_string_field[i])
            sku.append(combination_string_field[i].lower())
        elif combination_string_field[i] =="-":
            sku.append(combination_string_field[i+1].lower())
    string = ''.join(sku)
    return string

def get_unique_string(model_instance,combination_string,unique_string_id):
    unique=[]
    for i in combination_string:
        if i != "-":
            unique.append(i.lower())
    string = sorted(unique)
    string1 = ''.join(string)
    return string1


""" takes quality with respect to original quality in integer format,
    image_name under which image will be saved in string format,
    format (JPEG) is the preferred one,
    object which gives the model field name in which the image is to be saved,
    returns uploaded file value to be saved in the model field name"""
def upload_photo(quality: int, image_name: str, format: str, object):
    i = Image.open(object)
    thumb_io = BytesIO()
    i = i.convert('RGB')
    i.save(thumb_io, format='{format}'.format(format=format),
           quality=quality)
    value = InMemoryUploadedFile(thumb_io, None, 
                                 '{name}.jpeg'.format(name=image_name), 
                                 'image/jpeg', thumb_io.tell(),
                                  None)
    return value


"""cant be multithreaded as the process has to be synchronous"""
# class UploadThread(threading.Thread):

#     def __init__(self, quality: int, image_name: str, format: str, object):
#         self.quality = quality
#         self.image_name = image_name
#         self.format = format
#         self.object = object
#         threading.Thread.__init__(self)

#     def run(self):
#             i = Image.open(self.object)
#             thumb_io = BytesIO()
#             i = i.convert('RGB')
#             i.save(thumb_io, format='{format}'.format(format=self.format),
#                    quality=self.quality)
#             value = InMemoryUploadedFile(thumb_io, None, 
#                         '{name}.jpeg'.format(name=self.image_name), 
#                             'image/jpeg', thumb_io.tell(),
#                                 None)
#             return value
        

# class Util:
#     @staticmethod
#     def upload_photo(quality, image_name, format, object):
#         UploadThread(quality, image_name, format, object).start()





