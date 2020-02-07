from django.contrib import admin

from  .models import Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ("name",)


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [ReviewInLine]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    fieldsets = (
        (None, {
            "fields": (('title', 'tagLine'), )
        }),
        (None, {
            "fields": ('description', 'poster')
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



@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'ip')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie')



admin.site.register(RatingStar)

