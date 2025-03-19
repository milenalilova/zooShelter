from django.contrib import admin

from zooShelter.animals.models import AnimalCategory, Animal, AnimalImage


@admin.register(AnimalCategory)
class AnimalCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('personal_name', 'species')


@admin.register(AnimalImage)
class AnimalImageAdmin(admin.ModelAdmin):
    list_display = ('animal', 'is_primary')
