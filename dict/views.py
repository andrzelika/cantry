from django.shortcuts import render
from .models import Dictionary, Links

def links_things_list():
    l = Links.objects.all().order_by('code')
    t = Dictionary.objects.all().order_by('code')
    list_lt =(l,t)
    return list_lt

def mainpage(request):
    l=links_things_list()
    return render(request, 'dict/mainpage.html',{'links':l[0], 'things':l[1]})

def definition_view(request, ask):
    d = Dictionary.objects.filter(code=ask)
    l=links_things_list()
    return render(request, 'dict/definition.html',{'dictionary':d,
                                                   'links':l[0],
                                                   'things':l[1]})
