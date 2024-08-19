from django.contrib import admin
from first_app.models import *
from django.utils import timezone


def update_created_at(modeladmin, request, queryset):
    queryset.update(created_at=timezone.now())


update_created_at.short_description = "Update created_at to current time"


class BookInline(admin.TabularInline):
    model = Book
    extra = 1


# @admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInline]


# @admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Определение полей, которые будут отображаться в списке объектов модели
    list_display = ('title', 'author', 'published_date', 'created_at')
    # Задание полей, по которым будет производиться поиск
    search_fields = ('title', 'author')
    # Добавление боковых фильтров для быстрого поиска по указанным полям
    list_filter = ('author', 'published_date')
    # Определение порядка сортировки объектов в админке
    ordering = ('-author', 'title',)
    # Определение порядка и набора полей, которые будут отображаться в форме редактирования объекта
    fields = ('author', 'title', 'published_date', 'publisher', 'created_at')
    # Определение количества объектов, отображаемых на одной странице в списке
    list_per_page = 10
    actions = [update_created_at]


admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Post)
