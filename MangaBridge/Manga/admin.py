from django.contrib import admin

# Register your models here.
from.models import Manga, Fansub, Chapter
admin.site.register(Manga)
admin.site.register(Fansub)
admin.site.register(Chapter)