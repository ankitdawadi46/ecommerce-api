from dj_rql.filter_cls import RQLFilterClass
from products.models import variations_options


class variationvalueFilters(RQLFilterClass):
    MODEL = variations_options
    FILTERS = (
       { 'filters': ( 'id',
        'variationValue',
        'variation_id'),
       }
    )