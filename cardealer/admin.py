from django.contrib import admin

# Register your models here.

from .models import Dealers, Cars


class DealersAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'year', ]
    list_display_links = ['title', ]
    search_fields = ['title', 'location', 'year', ]
    list_filter = ['title', 'location', ]


class CarsAdmin(admin.ModelAdmin):
    list_display = ['brand', 'car_model', 'year_of_release', 'dealer', ]
    list_display_links = ['brand', 'car_model', 'dealer', ]
    search_fields = ['brand', 'car_model', 'year_of_release', 'dealer', ]
    list_filter = ['brand', 'car_model', 'year_of_release', 'dealer', ]


admin.site.register(Dealers, DealersAdmin)
admin.site.register(Cars, CarsAdmin)
