from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Manga, Chapter, Fansub
# Create your views here.
def Index(request):
    manga = Manga.objects.all()
    chapter = Chapter.objects.all().order_by("-relase_date")
    chapter_without_duplicates = list(set([c.manga for c in chapter]))[:20]
    fansub = Fansub.objects.all().values()

    mostview = manga.order_by("-manga_views")[:5]

    context= {
        "Manga": manga,
        "Chapter": chapter_without_duplicates,
        "Fansub": fansub,
        "Mostview": mostview,
    }

    template = loader.get_template("Index.html")

    return HttpResponse(template.render(context, request))

def MangaView(request, id):
    manga = Manga.objects.get(id = id)
    chapter = Chapter.objects.filter(manga = id)
    chapter_ = chapter.order_by("chapter_number")
    chapter_without_duplicates = list(set([c.chapter_number for c in chapter_]))
    available_fansubs = list(set([o.fansub for o in chapter]))

    manga.manga_views = manga.manga_views+1
    manga.save()

    context= {
        "Manga": manga,
        "Chapter": chapter,
        "Fansub": available_fansubs,
        "NoDuplicate": chapter_without_duplicates,
        #"AvailableChapter": chapters,
    }

    template = loader.get_template("MangaView.html")

    return HttpResponse(template.render(context, request))