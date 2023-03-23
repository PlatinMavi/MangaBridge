from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Manga, Chapter, Fansub, Duyuru, MangaCategory
# Create your views here.
def Index(request):
    manga = Manga.objects.all()
    chapter = Chapter.objects.all().order_by("manga_id" ,"-relase_date").distinct("manga_id")[:20]
    #chapter_without_duplicates = list(set([c.manga for c in chapter]))[:20]


    fansub = Fansub.objects.all().values()
    duyuru = Duyuru.objects.all()

    duyuru_len = len(duyuru)
    duyuru = duyuru[duyuru_len-1]

    mostview = manga.order_by("-manga_views")[:5]

    context= {
        "Manga": manga,
        "Chapter": chapter,
        "Fansub": fansub,
        "MostView": mostview,
        "Duyuru": duyuru,
    }

    template = loader.get_template("Index.html")

    return HttpResponse(template.render(context, request))

def MangaView(request, id):
    manga = Manga.objects.get(id = id)
    chapter = Chapter.objects.filter(manga = id)
    chapter_ = chapter.order_by("fansub","chapter_number")
    available_fansubs = list(set([o.fansub for o in chapter]))

    manga.manga_views = manga.manga_views+1
    manga.save()

    bolsay = chapter.order_by("-chapter_number")[0].chapter_number
    mangacategory = MangaCategory.objects.filter(manga=id)


    context= {
        "Manga": manga,
        "Chapter": chapter_,
        "Fansub": available_fansubs,
        "BolumSayi": bolsay,
        "Kategori": mangacategory,
    }

    template = loader.get_template("MangaView.html")

    return HttpResponse(template.render(context, request))