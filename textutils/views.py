from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    djtext = request.GET.get('text','default')
    context= {'name':'amjad', 'place':'Mars'}
    return render(request,'index.html',context)

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    removenewline = request.POST.get('removenewline','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')

    if removepunc =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_-'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        context = {'purpose':'Remove Punctuations', 'analyze_text': analyzed}   
        djtext = analyzed  
    
    if(fullcaps =="on"):
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        context = {'purpose':'Changed to Uppercase', 'analyze_text': analyzed}   
        djtext = analyzed         
    
    if(removenewline == "on"):
       analyzed = djtext.replace("\n", "").replace("\r", " ")
        
       context = {'purpose':'Remove New Lines','analyze_text': analyzed} 
       djtext = analyzed           
    
    if(extraspaceremove == "on"):
        analyzed = " ".join(djtext.split())
        
        context = {'purpose':'RemoveExtra space','analyze_text': analyzed}  
        djtext = analyzed           

    return render(request,'analyze.html',context) 


# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     djtext = request.GET.get('text', 'default')
#     context = {'name': 'amjad', 'place': 'Mars'}
#     return render(request, 'index.html', context)

# def analyze(request):
#     if request.method == 'POST':
#         djtext = request.POST.get('text', '')
#         removepunc = request.POST.get('removepunc', 'off')
#         fullcaps = request.POST.get('fullcaps', 'off')
#         removenewline = request.POST.get('removenewline', 'off')
#         extraspaceremove = request.POST.get('extraspaceremove', 'off')

#         if not djtext:
#             return HttpResponse("Please enter some text")

#         analyzed = djtext

#         if removepunc == "on":
#             punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_-'''
#             analyzed = ""
#             for char in djtext:
#                 if char not in punctuations:
#                     analyzed = analyzed + char
#             purpose = 'Remove Punctuations'

#         elif fullcaps == "on":
#             analyzed = ""
#             for char in djtext:
#                 analyzed = analyzed + char.upper()
#             purpose = 'Changed to Uppercase'

#         elif removenewline == "on":
#             analyzed = ""
#             for char in djtext:
#                 if char != "\n":
#                     analyzed = analyzed + char
#             purpose = 'Remove New Lines'

#         elif extraspaceremove == "on":
#             analyzed = ""
#             for index, char in enumerate(djtext):
#                 if not (djtext[index] == " " and djtext[index + 1] == " "):
#                     analyzed = analyzed + char
#             purpose = 'Remove Extra Spaces'

#         else:
#             return HttpResponse("Please select an operation")

#         context = {'purpose': purpose, 'analyze_text': analyzed}
#         return render(request, 'analyze.html', context)

#     else:
#         return HttpResponse("Invalid request")