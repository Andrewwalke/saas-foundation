from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit



def home(request):
    queryset = PageVisit.objects.all()
    title = "Sharu"
    my_context = {
        "line":title,
        "page_visit_count":queryset.count
    }
    PageVisit.objects.create()
    return render(request,"home.html",my_context)