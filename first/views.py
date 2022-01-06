from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'Forms.html')

def Analyzer(request):
    data = request.GET.get('text', 'This is Text')
    punct = request.GET.get('punc', 'off')
    cap = request.GET.get('cap', 'off')
    space= request.GET.get('space', 'off')
    count = request.GET.get('count', 'off')
    newl = request.GET.get('newl', 'off')
    if punct == 'on':
        analyzed = ""
        for char in data:
            with_punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
            if char not in with_punc:
                analyzed = analyzed + char
            prams = {'purpose': punct, 'analyzed_data':analyzed}
        data = analyzed
    if(cap=='on'):
        analyzed=""
        for char in data:
            analyzed = analyzed + char.upper()
            prams = {'purpose': 'Done', 'analyzed_data':analyzed}
        # return render(request, 'capital.html', prams)
        data = analyzed
    if(space=='on'):
        analyzed = ""
        for char in data:
            analyzed = analyzed + char.replace(" ", '')
            prams = {'purpose': 'Done', 'analyzed_data':analyzed}
        # return render(request, 'space.html',prams)
        data = analyzed
    if(count == 'on'):
        analyzed = 0
        for char in data:
            if (char.isalpha()):
                analyzed = analyzed+1
            prams = {'purpose': 'Done', 'analyzed_data':count}
        # return render(request, 'count.html',prams)
        data = analyzed
    if(newl == 'on'):
        analyzed = ""
        for char in data:
            char = char.replace('\n', '')
            analyzed = analyzed + char
            prams = {'purpose': 'Done', 'analyzed_data':analyzed}
        data = analyzed
    return render(request, 'punctuation.html', prams)
    
