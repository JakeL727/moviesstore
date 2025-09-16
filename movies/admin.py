from django.contrib import admin
from .models import Movie, Review, Report

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'user', 'date', 'is_removed')
    list_filter = ('is_removed', 'movie')
    search_fields = ('comment',)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'reporter', 'created_at', 'reason')
    list_filter = ('created_at',)
    search_fields = ('reason',)