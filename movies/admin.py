from django.contrib import admin
from django import forms

from  .models import Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Reviews

from ckeditor_uploader.widgets import CKEditorUploadingWidget 

class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ("name",)


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class MovieShotsInLine(admin.TabularInline):
    model = MovieShots
    extra = 1
    #readonly_fields = ("get_image",)

    #def get_image(self, obj):
        #return = mark_safe(f'<img src={obj.image.url} width="100" height="110"')
        
    #get_image.short_description = "Изображение"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [MovieShotsInLine, ReviewInLine]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ['publish', 'unpublish']
    form = MovieAdminForm
    #readonly_fields = ("get_image",)

    fieldsets = (
        (None, {
            "fields": (('title', 'tagLine'), )
        }),
        (None, {
            "fields": ('description', 'poster') #('poster', 'get_image')
        }),
        (None, {
            "fields": (('year', 'world_premiere', 'country'), )
        }),
        ('Actors', {
            "classes": ('collapse',),
            "fields": (('actors', 'directors', 'genres', 'category'), )
        }),
        (None, {
            "fields": (('budget', 'fees_in_usa', 'fees_in_world'), )
        }),
        ('Options', {
            "fields": (('url', 'draft'), )
        }),
    )

    #def get_image(self, obj):
        #return = mark_safe(f'<img src={obj.poster.url} width="100" height="110"')
        

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")


    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    
    publish.short_description = "Опубликовать"
    publish.allowed_permission = ('change', )

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permission = ('change', )

    #get_image.short_description = "Постер"


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'image') #get_image
    #readonly_fields = ("get_image",)

    #def get_image(self, obj):
        #return = mark_safe(f'<img src={obj.image.url} width="30" height="60"')
        
    #get_image.short_description = "Изображение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'ip')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie', 'image' ) #'get_image
    #readonly_fields = ("get_image",)

    #def get_image(self, obj):
        #return = mark_safe(f'<img src={obj.image.url} width="30" height="60"')
        
    #get_image.short_description = "Изображение"


admin.site.register(RatingStar)

admin.site.site_title = "Django Movies"
admin.site.site_header = "Django Movies"
