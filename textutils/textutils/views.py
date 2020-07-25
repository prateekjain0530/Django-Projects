#create this file
from django.http import HttpResponse
from django.shortcuts import render




def index(request):
    return render(request, 'index.html')
    #return HttpResponse("HOME")

def analyze(request):
    djtext = request.POST.get('text','default')
    djremovepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    analyzed = ""
    if djremovepunc == "on":
        punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''  
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations', 'analysed_text':analyzed}

    elif fullcaps=="on":
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed To uppercase', 'analysed_text':analyzed}
    
    elif newlineremover=="on":
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed = analyzed + char
        params = {'purpose':'New lines are removed', 'analysed_text':analyzed}
    
    elif spaceremover=="on":
        temp=djtext.split()
        analyzed = " ".join(temp)
        params = {'purpose':'Extra Spaces are removed', 'analysed_text':analyzed}
    else:
        return HttpResponse('ERROR!!!')
    
    return render(request, 'analyze.html', params)



