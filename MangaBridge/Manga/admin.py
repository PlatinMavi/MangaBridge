from django.contrib import admin

# Register your models here.
from.models import Manga, Fansub, Chapter, Duyuru
admin.site.register(Manga)
admin.site.register(Fansub)
admin.site.register(Chapter)
admin.site.register(Duyuru)